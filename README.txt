           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                KOTLIN MULTIPLATFORM APP WITH NIX BUILD
                              ENVIRONMENT

                             Perry Kundert
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


                          2024-11-25 11:11:00


Building a Kotlin app requires a multitude of dev dependencies, usually
supplied by installing random tools like Android Studio, etc.  This
produces a non-deterministic build environment. ([PDF]/[Text])

Using Nix, we provide a deterministic build environment, replicable
quickly on any suitable platform.

Table of Contents
─────────────────

1. Intelli-J Idea IDE
2. Create a Demo Kotlin App
3. TODO


[PDF] <./README.pdf>

[Text] <./README.txt>


1 Intelli-J Idea IDE
════════════════════

  Run
  ┌────
  │ $ nix-shell
  └────


  to gain access to `kdoctor` to analyze your development environment,
  and `idea` to start Intelli-J Idea.


2 Create a Demo Kotlin App
══════════════════════════

  Follow
  <https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-create-first-app.html>
  to create a demo app.  This is how we produced GreetingsKMP.zip.


3 TODO
══════

  • Provide Nix Flake environment w/ build tools and SDKs:
    <https://github.com/tadfisher/android-nixpkgs>
  • Add access to Holochain dev environment with
    <https://github.com/spartan-holochain-counsel/nix-overlay>
