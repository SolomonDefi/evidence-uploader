# Solomon Evidence Uploader

This repository contains the [frontend](./frontend/README.md) and [backend](./backend/README.md) for the Solomon evidence uploading system.
See the READMEs in those folders for installation instructions and more technical details.

The purpose of the uploader is to provide a simple interface for uploading evidence links to the blockchain during escrow disputes. Links must exist for the
duration of the dispute (generally a maximum of 2 months). There are several methods for uploading evidence, and it is straightforward to
add more.

1. User provides their own link
2. User provides files and the `backend` uploads to an S3-compatible data store
3. (TBD) Pin on an IPFS node for the duration of a dispute

Currently, only Metamask is supported as a wallet provider for posting the link to the blockchain, but WalletConnect and other methods may
be added in the future.

A hosted frontend and backend will be provided by Solomon, based on this repository.
