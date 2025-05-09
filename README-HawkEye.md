# Delphi in HawkEye

This README file describes how to reproduce the model communication cost propfiling results from Delphi shown in Table 6 and Table 7 of the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025).

## Linux
 - Ubuntu 20.04 

## Required Packages And Tested Versions
The required packages are listed below. It might also work with other versions. 
 - g++ 11.4.0
 - cmake 3.21.1
 - pkg-config 0.29.1
 - gcc 11.4.0
 - libssl-dev 1.1.1f-1ubuntu2.24
 - libclang-dev 1:10.0-50~exp1
 - rustup 1.27.1
 - rustc 1.83.0

Except for `rustup` and `rustc`, the above packages can be installed directly using `sudo apt-get install <package>` on Linux. For `rustup`, run the following command and follow the instructions.
```
sudo apt-get install curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
After running the above command successfully, you may encounter the following prompt:
```
Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, you need to source
the corresponding env file under $HOME/.cargo.

This is usually done by running one of the following (note the leading DOT):
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
source "$HOME/.cargo/env.fish"  # For fish
```
Choose the appropriate command to run based on your shell type.
Once `rustup` is installed, you can install `rustc` by running the following command:
```
rustup install nightly
```

## Build the environment
```
cd Delphi-HawkEye/rust
cargo +nightly build --release
```

## Compile models and run profiling processes
Open two terminals and run the following two commands in Delphi-HawkEye/rust simultaneously:
```
cargo +nightly run --bin resnet32-server --release --all-features -- -l 0 > resnet32_log.txt
cargo +nightly run --bin resnet32-client --release --all-features -- -l 0 -i 127.0.0.1
```
After running the above commands, a text file named resnet32_log.txt will be generated in the `Delphi-HawkEye/rust` folder. Then, run the following command to get the profiling results at any terminal:
```
cd ..
python report.py resnet32_log.txt
```
For the profiling results of MiniOnn, you can obtain them by simply replacing `resnet32` with `MiniOnn` in the above commands.
