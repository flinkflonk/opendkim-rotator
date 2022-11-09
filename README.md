OpenDKIM rotator
================

Does exactly what it says on the box, at least once it's finished.

Takes your opendkim configuration to find out about your keys and
rotates them, with a configurable DNS backend (I haven't decided
yet if I want it to modify my DNS server's zonefiles directly and
reload it or if I just want to spit out the info to do it manually,
so I'll probably do both :) )

Configuration should be for choosing a DNS backend, so maybe I'll
rather make it configuration-less and choose the backend by
command line option. We really have enough configuration files.

Info about keys and such is kept in a database in a predefined
place (/var/cache/opendkim-rotator/db.db? Something like that).
We need to keep info over several runs because DNS is slow and
mail is fast. We shouldn't sign with keys that haven't propagated
out to all DNS caches yet. Also, old key deletion should be delayed
until any emails signed with them should have been received.

Michael Hinz, 2017-01-10

A working version is running at my work since 2019 and rotating
DKIM keypairs for roughly 3800 domains every three months. I'm
working on a new version, which is both more generic (therefore
open-sourcable - the running version is very specific to our DNS
and SMTP server installation) and more user-friendly (not just a
script, but a full DJango-App providing both an administration
interface and monitoring).

Michael Hinz, 2022-06-12

I'm hereby abandoning this project as I have started a new one
based on the code from work (as mentioned above). This code
is archived for now and will be deleted when the first working
version of the new project is uploaded to github.com (for now
it lives on my private server, although it is publically
visible I'm not prepared to stagger all the bots scanning
github on that server, so the URL can be gotten by writing
me).

Michael Hinz, 2022-11-10
