{ pkgs ? import ./nixpkgs.nix {} }:
  let
    unstable = import <unstable> { config.allowUnfree = true; };
    java = pkgs.zulu17;
    gradle = pkgs.gradle.override { inherit java; };
    kotlin = pkgs.kotlin.override { jre = java; };
    intellij = unstable.jetbrains.idea-ultimate;
  in
  pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      java
      gradle
      kotlin
      intellij
      # android-studio  # Linux only?
      kdoctor
      libGL
      xorg.libX11
      fontconfig
    ];

    shellHook = ''
      export BASE_DIR=$(pwd)
      mkdir -p $BASE_DIR/.share
      
      if [ -L "$BASE_DIR/.share/java" ]; then
        unlink "$BASE_DIR/.share/java"
      fi
      ln -sf ${java}/lib/openjdk $BASE_DIR/.share/java

      if [ -L "$BASE_DIR/.share/gradle" ]; then
        unlink "$BASE_DIR/.share/gradle" 
      fi
      ln -sf ${gradle}/lib/gradle $BASE_DIR/.share/gradle
      export GRADLE_HOME="$BASE_DIR/.share/gradle"

      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${
        pkgs.lib.makeLibraryPath [
          kotlin
          pkgs.libGL
          pkgs.xorg.libX11
          pkgs.fontconfig
        ]
      };
    '';
  }
