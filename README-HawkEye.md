# Delphi in HawkEye

This README file describes how to reproduce the model communication cost propfiling results from Delphi shown in Table 6 and Table 7 of the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025).

## Required Packages
 - g++ 
 - cmake
 - pkg-config
 - gcc
 - libssl-dev
 - libclang-dev
 - rustup
 - rust

Except for `rustup` and `rust`, the above packages can be installed directly using `sudo apt-get install <package>` on Linux. For `rustup`, run the following command and follow the instructions.
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
After installing `rustup`, install the `rust` by running the following command:
```
rustup install nightly
```

## Build the environment

```
cd delphi/rust
cargo +nightly build --release
```

## Compile models and run profiling processes
Open two terminals and run the following two commands simultaneously:
```
cd rust
cargo +nightly run --bin resnet32-server --release --all-features -- -l 0 > resnet32_log.txt
cargo +nightly run --bin resnet32-client --release --all-features -- -l 0 -i 127.0.0.1
```
After running the above commands, a text file named resnet32_log.txt will be generated in the `Delphi-HawkEye/rust` folder. Then, run the following command to get the profiling results at any terminal:
```
cd ..
python report.py resnet32_log.txt
```
For the profiling results of MiniOnn, you can obtain them by simply replacing `resnet32` with `MiniOnn` in the above commands.