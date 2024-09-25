# Otterdog

Our organization configs are managed on [.eclipsefdn](https://github.com/eclipse-pass/.eclipsefdn)
using the [Otterdog tool](https://gitlab.eclipse.org/eclipsefdn/security/otterdog)

Our first project will be to manage secrets via [bitwarden](/docs/infra/bitwarden.md).

## Pushing GitHub Infra Changes

To make changes, you must push a [forked PR like this one](https://github.com/eclipse-pass/.eclipsefdn/pull/1).

![Sample PR](/docs/assets/otterdog/otterdog_sample_pr.png)


## Configurations

The base configuration is [eclipse-pass.jsonnet](https://github.com/eclipse-pass/.eclipsefdn/blob/main/otterdog/eclipse-pass.jsonnet),
and can be monitored at [eclipse-pass.org/.eclipsefdn](https://eclipse-pass.org/.eclipsefdn/)

![Otterdog Config Monitoring](/docs/assets/otterdog/dashboard.png)

The base entry for jsonnett configs is via

```javascript
local orgs = import 'otterdog-defaults.libsonnet';
```

## Managing Passwords

If you are adding new secrets, then please ensure you
[securely share those secrets with Eclipse Foundation operations team](/docs/infra/sharing_secrets.md)


## Playground (Online Editor)

From the [monitoring application](https://eclipse-pass.org/.eclipsefdn/) you can access a [otterdog playground](http://eclipse-pass.org/.eclipsefdn/playground/)

![Otterdog Playground](/docs/assets/otterdog/playground.png)

## Installing Locally

If you are testing github integrations, you will need to [install Otterdog locally](https://otterdog.readthedocs.io/en/latest/install/)

Below is a summary of the [installation guide above](https://otterdog.readthedocs.io/en/latest/install/).
If you run into problems, then please read the source installation guide and update these docs.

You will need the following tools

```bash
python3 --version # 3.10+, tested on 3.11.4
pip --version     # any,   tested on 23.2
poetry --version  # any,   tested on 1.4.2
go version        # 1.13+, tested on 1.20.5
jb --version      # any,   tested on 'dev' (aka 0.5.1 as shown in troubleshooting below)
bw -v             # any,   tested on 2023.9.0
```

Now you can clone the [Otterdog repo](https://gitlab.eclipse.org/eclipsefdn/security/otterdog/)
and build it locally

```bash
# Somewhere outside of the eclipse-pass repos
git clone git@gitlab.eclipse.org:eclipsefdn/security/otterdog.git
cd otterdog
make init
```

You now have `otterdog` installed locally.

```bash
otterdog --version
# otterdog.sh, version 0.3.0.dev0
```

### Troubleshooting

#### jb / jsonnet-bundler not found

Here's how you install [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler) (aka `jb`)

```
go install -a github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb@v0.5.1
```

Note that [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler) was installed to a `$HOME/go/bin` which was NOT
on our path, so I had to add that to ensure `jb` was accessible.

```bash
# in your ~/.bash_profile or similar
PATH="$HOME/go/bin:$PATH"
```

#### bw / bitwarden not found

Here's how you install [bitwarden](https://github.com/bitwarden/clients) (aka `bw`).

The installation uses `snap`, but (home)`brew` also works

```bash
brew install bitwarden-cli
```

#### .local/bin/otterdog: No such file or directory

If you see something like

```bash
test -f ~/.local/bin/otterdog || ln -s /Users/aforward/sin/projects/eclipse-pass/otterdog/otterdog.sh ~/.local/bin/otterdog
ln: /Users/aforward/.local/bin/otterdog: No such file or directory
make: *** [init] Error 1
```

Then ensure that you have a `~/.local/bin` to receive the file, and that is also on your path

```bash
mkdir -p ~/.local/bin

# in your ~/.bash_profile or similar
PATH="$HOME/.local/bin:$PATH"
```

#### How do I get the github organization ID from the UI

You will need to **Inpsect** the org page and look for `organization:`

![GitHub Organization ID](/docs/assets/github/ui_get_org_id.png)
