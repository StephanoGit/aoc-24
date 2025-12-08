{
  description = "Python Jupyter environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            (python.withPackages (
              ps: with ps; [
                jupyter
                numpy
                torch
                tqdm
                pandas
                ipython
                opencv4
                pycocotools
                pillow
                torchvision
                torchaudio
                torchsummary
                matplotlib
                kaggle
                mne
              ]
            ))
            pkgs.wget
            pkgs.git
          ];

          shellHook = ''
            echo "🐍 Python Jupyter environment loaded"
            echo "Run: jupyter notebook"
          '';
        };
      }
    );
}
