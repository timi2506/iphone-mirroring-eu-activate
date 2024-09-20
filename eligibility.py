import os
import platform
import sys
import traceback
from pathlib import Path

import click
import requests
from packaging.version import parse as parse_version
from pymobiledevice3.cli.cli_common import Command
from pymobiledevice3.exceptions import NoDeviceConnectedError, PyMobileDevice3Exception
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3.services.installation_proxy import InstallationProxyService

from sparserestore import backup, perform_restore


def exit(code=0):
    if platform.system() == "Windows" and getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        input("Press Enter to exit...")

    sys.exit(code)


@click.command(cls=Command)
@click.pass_context
def cli(ctx, service_provider: LockdownClient) -> None:
    os_names = {
        "iPhone": "iOS",
        "iPad": "iPadOS",
        "iPod": "iOS",
        "AppleTV": "tvOS",
        "Watch": "watchOS",
        "AudioAccessory": "HomePod Software Version",
        "RealityDevice": "visionOS",
    }

    device_class = service_provider.get_value(key="DeviceClass")
    device_build = service_provider.get_value(key="BuildVersion")
    device_version = parse_version(service_provider.product_version)

    if not all([device_class, device_build, device_version]):
        click.secho("Failed to get device information!", fg="red")
        click.secho("Make sure your device is connected and try again.", fg="red")
        return

    os_name = (os_names[device_class] + " ") if device_class in os_names else ""
    click.secho(f"{os_name}{device_version} ({device_build})")

    back = backup.Backup(
        files=[
            backup.Directory("", "RootDomain"),
            backup.Directory("Library", "RootDomain"),
            backup.Directory("Library/Preferences", "RootDomain"),
            
            # Feature flags are probably unnecessary to change, since most of the SAE-related stuff is already enabled by default.
            backup.Directory(
                "",
                f"SysContainerDomain-../../../../../../../../var/preferences/FeatureFlags",
                owner=33,
                group=33,
            ),
            backup.ConcreteFile(
                "",
                f"SysContainerDomain-../../../../../../../../var/preferences/FeatureFlags/Global.plist",
                owner=33,
                group=33,
                #contents=open("xezrunner/FeatureFlags.plist", "rb").read(),  # Stage 1
                contents=open("xezrunner/empty.plist", "rb").read(),         # Stage 2
            ),

            # Eligibility (bypasses EU too!)
            backup.Directory(
                "",
                f"SysContainerDomain-../../../../../../../../var/db/os_eligibility/",
                owner=33,
                group=33,
            ),
            backup.ConcreteFile(
                "",
                f"SysContainerDomain-../../../../../../../../var/db/os_eligibility/eligibility.plist",
                owner=33,
                group=33,
                contents=open("xezrunner/eligibility.plist", "rb").read(),
                inode=0,
            ),

            # backup.ConcreteFile(
            #     "",
            #     "SysContainerDomain-../../../../../../../../var/.backup.i/var/root/Library/Preferences/temp",
            #     owner=501,
            #     group=501,
            #     contents=b"",
            # ),
            
            # Don't restore!
            backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""),
        ]
    )

    try:
        perform_restore(back, reboot=False)
    except PyMobileDevice3Exception as e:
        if "Find My" in str(e):
            click.secho("Find My must be disabled in order to use this tool.", fg="red")
            click.secho("Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again.", fg="red")
            exit(1)
        elif "crash_on_purpose" not in str(e):
            raise e

    click.secho("Success!", fg="green")

    if False:
        with DiagnosticsService(service_provider) as diagnostics_service:
            click.secho("Rebooting device...", fg="green")
            diagnostics_service.restart()


def main():
    try:
        cli(standalone_mode=False)
    except NoDeviceConnectedError:
        click.secho("No device connected!", fg="red")
        click.secho("Please connect your device and try again.", fg="red")
        os.system("chmod +x rerun.sh")
        os.system("bash rerun.sh")
    except click.UsageError as e:
        click.secho(e.format_message(), fg="red")
        click.echo(cli.get_help(click.Context(cli)))
        exit(2)
    except Exception:
        click.secho("An error occurred!", fg="red")
        click.secho(traceback.format_exc(), fg="red")
        exit(1)

    quit()


if __name__ == "__main__":
    main()
