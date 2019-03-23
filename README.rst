AddSSHkeys:  Add Keys to SSH Agent
==================================

| Version: 0.0.2
| Released: 2019-03-23
|

*AddSSHkeys* adds all of your keys to SSH Agent in one operation. It can work 
with `Avendesora <https://avendesora.readthedocs.io>`_ to keep your passphrases 
secure.

Please report all bugs and suggestions to addsshkeys@nurdletech.com

Getting Started
---------------

You download and install *AddSSHkeys* with::

    pip3 install --user addsshkeys

Once installed, you will need at least one configuration file. The files should 
be placed in ~/.config/addsshkeys. The default file is *config*.

Configurations can be found in: ~/.config/addsshkeys.
They are Python files.  The default configuration is *config*.

The following settings may be given in your config files.


**ssh_add**

The name of the command that adds keys to your SSH agent. By default, 'ssh-add' 
is used.

**ssh_keys**

This setting is required.  It contains a dictionary of dictionaries that 
contains information about each key.  The primary dictionary contains a name and 
the values for each key. The values are held in a dictionary that may contain 
three fields:

*paths*

This is required and contains the paths to one or more SSH private key files.  
It may be a list of strings, or a single string that is split.  If a relative 
path is given, it is relative to ~/.ssh.

*account*

This gives the name of the Avendesora account that holds passphrase for the 
keys. If present, Avendesora will be queried for the passphrase.

*passphrase*

This is required if *account* is not given, otherwise it is optional.  If 
*account* is given, it is the name of the passphrase field in Avendesora, which 
defaults to 'passcode'. If account is not given, it is the passphrase itself. In 
this case, the settings file should only be readable by the user.

**config_file_mask**

An integer that determines if a warning should be printed about the the
config file permissions being too loose.  The permissions are only checked
if the file is found to contain a passphrase. Default is 0o077.  Set to
0o000 to disable the warning. Set to 0o077 to generate a warning if the
configuration directory is readable or writable by the group or others. Set
to 0o007 to generated a warning if the directory is readable or writable by
others.

Here is an example configuration file::

    ssh_keys = dict(
        primary = dict(
            paths = 'primary-ed25519 primary-rsa',
            account = 'primary-ssh-key',
        ),
        digitalocean = dict(
            paths = 'digitalocean',
            account = 'digitalocean-ssh-key',
        ),
        github = dict(
            paths = 'github',
            passphrase = 'canard apply trousseau forgive',
        ),
        backups = dict(
            paths = 'dumper',
            account = 'dumper-ssh-key',
        ),
    )


Running AddSSHkeys
------------------

Once configured, you can run *AddSSHkeys* with the default configuration using::

    addsshkeys

And you can run it with a particular configuration using::

    addsshkeys <config>

where ``<config>`` is the name of the configuration you wish to use. In this way 
you can have several bundles of keys that you can load as needed.


Releases
--------
**Latest Development Version**:
    | Version: 0.0.2
    | Released: 2019-03-23
