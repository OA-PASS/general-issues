# Sharing GitHub Secrets

Using [otterdog in .eclipsefdn](https://github.com/eclipse-pass/.eclipsefdn)
here is the process of adding secrets to our GitHub organization.

## PASSword Configs in Otterdog

Our
[eclipse foundation otterdog configs](https://gitlab.eclipse.org/eclipsefdn/security/otterdog#bitwarden)
supports the [pass(word store)](https://www.passwordstore.org) application for secrets management.

An [example pull request adding a password](https://github.com/eclipse-pass/.eclipsefdn/pull/1) shows
the desired end-state of our to add secrets.  Make sure to use the
[otterdog playground](http://eclipse-pass.org/.eclipsefdn/playground/)
to help write _correct_ jsonnett.

The structure for passwords is

```jsonnett
orgs.newOrgSecret('<NAME>_<CUSTOMFIELD>') {
  value: "pass:bots/technology.pass/<name>/<customfield>",
},
```

For example,

```jsonnett
orgs.newOrgSecret('HELLOWORLD_QUEST') {
  value: "pass:bots/technology.pass/helloworld/quest",
},
orgs.newOrgSecret('HELLOWORLD_COLOR') {
  value: "pass:bots/technology.pass/helloworld/color",
},
```

## Storing Secrets

### Sharing Directly via PGP Encrypted email.

Until Bitwarden is configured, secrets will be sent directly
using `gpg encrypted mail` and [this gpg public key](https://keyserver.ubuntu.com/pks/lookup?search=thomas.neidhart%40eclipse-foundation.org&fingerprint=on&op=index)
to encrypt the email.

If Bitwarden is configured, please skip to the next section

```
Hi Thomas,

Can you add these secrets to our .eclipsefdn account based on this pull request.
https://github.com/eclipse-pass/.eclipsefdn/pull/1

pass:bots/technology.pass/helloworld/quest : Holy Grail
pass:bots/technology.pass/helloworld/color : Blue Not Green

When ready, please approve the merge and apply the
changes in our PR.

Thank you,

Open Access PASS Team
```

### Storing Secrets in Bitwarden Secrets Manager

We will use
[bitwarden to store our passwords](/docs/infra/bitwarden.md)
and share those.

![Naming conventions](/docs/assets/bitwarden/naming_conventions.png)

Ideally these passwords are then integrated directly into our
[.eclipsefdn](https://github.com/eclipse-pass/.eclipsefdn) as document
far below, but for now we have an interim step to manage the
passwords indirectly using the [pass(word store)](https://www.passwordstore.org)
notation.

###a Merging Passwords

We can use the `secret_handshake` for sharing secrets with Eclipse Foundation (EF).

![Secret handshake](/docs/assets/bitwarden/secret_handshake.png)

We can then use that `secret_handshake` to encrypt our (for eaxmple) _helloworld_ password with EF.

![Create a secret share](/docs/assets/bitwarden/create_secret_share.png)

We will need that URL

![Secret share URL](/docs/assets/bitwarden/secret_share_url.png)

And the URL will look like

```
https://send.bitwarden.com/#R9KxxMqJiESP87ClATIJ-g/7_fOjgbzNTDWzyJqALdy_A
```

This can be dropped into the [.eclipsefdn project](https://github.com/eclipse-pass/.eclipsefdn)
for the configs pull request ([an example PR here](https://github.com/eclipse-pass/.eclipsefdn/pull/1))

Separately, we need to share that `secret_handshake` over email using `gpg encrypted mail`.
Se can use [this gpg public key](https://keyserver.ubuntu.com/pks/lookup?search=thomas.neidhart%40eclipse-foundation.org&fingerprint=on&op=index)
for sending those emails.

A sample email (please replace the placeholdrs)

```
Hi Thomas,

This secret

ABC123

Will decrypt our passwords in
https://send.bitwarden.com/#R9KxxMqJiESP87ClATIJ-g/7_fOjgbzNTDWzyJqALdy_A

As part of this pull-request
https://github.com/eclipse-pass/.eclipsefdn/pull/1

When ready, please approve the merge and apply the
changes in our PR.

Thank you,

Open Access PASS Team
```

## Bitwarden Configs in Otterdog

At present, we cannot share Bitwarden passwords directly in our
[eclipse foundation otterdog configs](https://gitlab.eclipse.org/eclipsefdn/security/otterdog#bitwarden)

When we can, let's revisit these confirmations.

### Add Bitwarden Items

Using jsonnett based on the outputs from the
[otterdog playground](http://eclipse-pass.org/.eclipsefdn/playground/).
we can add a new organization and then incorporate items.

```javascript
orgs.newOrg('eclipse-pass') {
  credentials+: [{
      "provider": "bitwarden",
      "item_id" : "23801ca4-fd27-446c-b5af-b07b0108f443"
    },
  ],
}
```

### Add Organization Secrets

And then we can specify secrets based on the structure of `bitwarden:<item_id>@<field_name>`.

Here is documentation on managing [organization secrets](https://otterdog.readthedocs.io/en/latest/reference/organization/secret/)

```javascript
orgs.newOrg('eclipse-pass') {
  secrets+: [
    orgs.newOrgSecret('HELLO_WORLD_QUEST') {
      value: "bitwarden:23801ca4-fd27-446c-b5af-b07b0108f443@quest",
    },
    orgs.newOrgSecret('HELLO_WORLD_COLOR') {
      value: "bitwarden:23801ca4-fd27-446c-b5af-b07b0108f443@color",
    },
  ],
}
```

Please refer to [bitwarden for specifics on password management](/docs/infra/bitwarden.md)
