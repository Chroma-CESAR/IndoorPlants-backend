# IndoorPlants

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd IndoorPlants
```

### Install Justfile and gum

- On macOS, you can use Homebrew to install Justfile and gum:

```bash
brew install just
brew install gum
```

- On Linux, you can use the following commands to install Justfile and gum:

```bash
sudo apt-get install just
sudo snap install gum
```

- On Windows, you can use the following commands to install Justfile and gum:

```bash
winget install --id Casey.Just --exact
winget install charmbracelet.gum
or
scoop install just
scoop install charm-gum
```

### Install dependencies

```bash
just
```

Select the option `install-requirements` to install the required dependencies and create venv.
