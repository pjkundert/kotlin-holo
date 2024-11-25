SHELL		= /bin/bash

#
# nix-...:
#
# Use a NixOS environment to execute the make target, eg.
#
#     nix-...
#
# Depends on the nixos-unstable channel
#
nix-%:
	nix-channel --add https://nixos.org/channels/nixos-unstable unstable
	nix-channel --update
	nix-shell $(NIX_OPTS) --run "make $*"

