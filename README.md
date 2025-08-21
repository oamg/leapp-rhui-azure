# Official repository of `leapp-rhui-azure` and `leapp-rhui-azure-sap` packages

## About `leapp-rhui-azure` packages
The `leapp-rhui-azure` (or `leapp-rhui-azure-sap`) provides required additional
files for in-place upgrades using [Leapp](https://github.com/oamg/leapp-repository)
of RHEL pay-as-you-go images on Azure. Currently, these support files consist
only of a single repofile (and possibly a GPG key). This is thanks to Leapp being
able to download & install RHUI client of the target system early during the upgrade
process. It is because of this installation of the target RHUI client that
the `leapp-rhui-azure` packages have Python dependencies.

## Building
To build the `leapp-rhui-azure` and `leapp-rhui-azure-sap` packages, the `./build.sh` script
is provided. Packages for RHEL `$RHEL_VER` can be built by running
```bash
./build.sh $RHEL_VER
```

For example, `./build.sh 8` will build the packages for RHEL 8.
