from setuptools import setup, find_packages

setup(name='ninfo-plugins',
    version='0.1.13k',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
    ],
    entry_points = {
        'ninfo.plugin': [
            'nfi_stats      = ninfo_plugins.nfi_stats.nfi_stats_plugin',
            'ipblocker      = ninfo_plugins.ipblocker.ipblocker_plugin',
            'tm             = ninfo_plugins.tm.tm_plugin',
            'snort          = ninfo_plugins.snort.snort_plugin',
            'cif            = ninfo_plugins.cif.cif_plugin',
            'pinginventory  = ninfo_plugins.pinginventory.pinginventory_plugin',
            'netdisco       = ninfo_plugins.netdisco.netdisco_plugin',
        ]
    }
) 
