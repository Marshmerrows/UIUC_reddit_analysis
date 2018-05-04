virtualenv env
source env/bin/activate

pip install beautifulsoup4
pip install selenium

#!/bin/bash
# download and install latest geckodriver for linux or mac.
# required for selenium to drive a firefox browser.

install_dir="env/bin/"
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
if [[ $(uname) == "Darwin" ]]; then
  url=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
        python -c "import sys, json; print(next(item['browser_download_url'] \
        for item in json.load(sys.stdin)['assets'] if 'macos' in item.get('browser_download_url', '')))")
elif [[ $(uname) == "Linux" ]]; then
  url=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
        python -c "import sys, json; print(next(item['browser_download_url'] \
        for item in json.load(sys.stdin)['assets'] if 'linux64' in item.get('browser_download_url', '')))")
else
  echo "can't determine OS"
  exit 1
fi
curl -s -L "$url" | tar -xz
chmod +x geckodriver
mv geckodriver "$install_dir"
echo "installed geckodriver binary in $install_dir"
