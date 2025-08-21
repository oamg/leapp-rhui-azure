#!/bin/bash

exit_with_error () {
    error_str=$1
    echo Error: $error_str && exit 1
}

print_help() {
    echo "Usage: ./build.sh RHEL_VERSION"
    echo "  where RHEL_VERSION is 7, 8, or 9."
    echo "For example, to build leapp-rhui-azure packages for RHEL 8, use"
    echo "  ./build.sh 8"
}

TARGET_RHEL_VERSION=$1

case $TARGET_RHEL_VERSION in
    7|8|9) : ;;
    *)
       print_help
       exit_with_error "Invalid target version: $TARGET_RHEL_VERSION. Valid versions: 7, 8, 9." ;;
esac

#
# Variables controlling the build - defaults. If you need to change them for specfic variant & target version, do so bellow
#
target_rhel_rpm_str="el$TARGET_RHEL_VERSION"  # el7, el8, etc.
specfile_name="leapp-rhui-azure.spec"
rpm_name="leapp-rhui-azure"
build_dir=./out
clean_build_dir=y

#
# Chroot selection based on target RHEL version
#
chroot_name="rhel-7-x86_64"
case $TARGET_RHEL_VERSION in
    7)
        chroot_name="rhel-7-x86_64" ;;
    8)
        chroot_name="centos-stream+epel-8-x86_64" ;;  # Use centos chroots so that it is easier to build on non-RHEL systems
    9)
        chroot_name="centos-stream+epel-9-x86_64" ;;
esac


specfile_path=$specfile_name
leapp_pkg_version=$(cat $specfile_path | grep Version | head -1 | tr -s ' ' | cut -d' ' -f2)
rpm_name_with_version=$rpm_name-$leapp_pkg_version

# 0. Clean old build artifacts
if [[ $clean_build_dir == y && -d $build_dir ]]; then
    echo "Removing the old build directory."
    rm -r $build_dir
fi

# 1. Create a .tar.gz archive with package sources:
mkdir -p "$build_dir/$rpm_name_with_version"
cp -r src "$build_dir/$rpm_name_with_version/src"
pushd $build_dir || exit_with_error "Failed to enter the build directory $build_dir"
tar cvzf "$rpm_name_with_version.tar.gz" "$rpm_name_with_version"
popd || exit_with_error "Failed to exit the build directory $build_dir"

# 2. Create a SRMP from the package sources
mock -r "$chroot_name" --spec=$specfile_path --sources="$build_dir/$rpm_name_with_version.tar.gz" --buildsrpm --resultdir $build_dir/srpm-result

# 3. Build RPM from the created SRPM
mock -r "$chroot_name" rebuild "$(find $build_dir/srpm-result -regex "$build_dir/srpm-result/$rpm_name_with_version-[0-9]+.$target_rhel_rpm_str.src.rpm")" --resultdir $build_dir/rpm-result

# The package can be found at $build_dir/rpm-result
