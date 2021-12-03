# JMC Agent Packaging

copr repository available at: https://copr.fedorainfracloud.org/coprs/almac/jmc-agent/

## Using the contents of this repo

### Fetch the JMC sources
`$ bash fetch-sources.sh`

### Building the source rpm
`$ fedpkg srpm`

optionally, can create a Fedora version-specific srpm:
`$ fedpkg --release f33 srpm` would create a srpm for Fedora 33

### Building the package locally (mock)
If I'm looking to create a mock build for Fedora 33 using the first iteration of this package, my command might look something like:</br>
`$ mock -r fedora-33-x86_64 ./jmc-agent-1.0.1-1.fc33.src.rpm`

optionally, can add `--postinstall` to install the resulting `.rpm` once it is built

### Building the package in copr
First, set up a copr project for your builds. (https://copr.fedorainfracloud.org/)</br>

In your new project, create a build by navigating to the "Builds" page, and select the button "New Build". On this page you can select "Upload" as the source type, and select the source rpm built two steps ago. Select the chroots of interest and build it.</br>
