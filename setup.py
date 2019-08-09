from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='SoberLife II',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: pygame',
        'Topic :: Games/Entertainment :: Board Games',
    ],
    include_package_data=True,
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,
    windows=[{
        "script": "SoberLifeII-script.pyw",
        "icon_resources": [(1, "./assets/icon.ico")],
        "dest_base":"SoberLifeII"
    }],
    packages=find_packages(),
    install_requires=requirements,
    version='0.0.1',
    entry_points={
        'gui_scripts': [
            'SoberLifeII = SoberLifeII:main',
        ],
    },
)
