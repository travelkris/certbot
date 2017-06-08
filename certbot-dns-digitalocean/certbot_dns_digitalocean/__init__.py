"""
The `~certbot_dns_digitalocean.dns_digitalocean` plugin automates the process of
completing a ``dns-01`` challenge (`~acme.challenges.DNS01`) by creating, and
subsequently removing, TXT records using the DigitalOcean API.


Named Arguments
---------------

==========================================  ===================================
``--dns-digitalocean-credentials``          DigitalOcean credentials_ INI file.
                                            (Required)
``--dns-digitalocean-propagation-seconds``  The number of seconds to wait for
                                            DNS to propagate before asking the
                                            ACME server to verify the DNS
                                            record.
                                            (Default: 10)
==========================================  ===================================

Credentials
-----------

Use of this plugin requires a configuration file containing DigitalOcean API
credentials, obtained from your DigitalOcean account's `Applications & API
Tokens page <https://cloud.digitalocean.com/settings/api/tokens>`_.

.. code-block:: ini
   :name: credentials.ini
   :caption: Example credentials file:

   # DigitalOcean API credentials used by Certbot
   dns_digitalocean_token = 0000111122223333444455556666777788889999aaaabbbbccccddddeeeeffff

The path to this file can be provided interactively or using the
``--dns-digitalocean-credentials`` command-line argument. Certbot records the
path to this file for use during renewal, but does not store the file's contents.

.. caution::
   You should protect these API credentials as you would the password to your
   DigitalOcean account. Users who can read this file can use these credentials
   to issue arbitrary API calls on your behalf. Users who can cause Certbot to
   run using these credentials can complete a ``dns-01`` challenge to acquire
   new certificates or revoke existing certificates for associated domains,
   even if those domains aren't being managed by this server.

Examples
--------

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``

   certbot certonly \\
     --dns-digitalocean \\
     --dns-digitalocean-credentials ~/.secrets/certbot/digitalocean.ini \\
     -d example.com

.. code-block:: bash
   :caption: To acquire a single certificate for both ``example.com`` and
             ``www.example.com``

   certbot certonly \\
     --dns-digitalocean \\
     --dns-digitalocean-credentials ~/.secrets/certbot/digitalocean.ini \\
     -d example.com \\
     -d www.example.com

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``, waiting 60 seconds
             for DNS propagation

   certbot certonly \\
     --dns-digitalocean \\
     --dns-digitalocean-credentials ~/.secrets/certbot/digitalocean.ini \\
     --dns-digitalocean-propagation-seconds 60 \\
     -d example.com

"""
