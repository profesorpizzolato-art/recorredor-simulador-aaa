  "name": "Python 3",
  
  "customizations": {
    "codespaces": {
      "openFiles": [
        "README.md",
        "reco.py"
      ]
    },
    "vscode": {
      "settings": {},
      "extensions": [
        "ms-python.python",
           ]
    }
  },
  "updateContentCommand": "[ -f packages.txt ] && sudo apt update && sudo apt upgrade -y && sudo xargs apt install -y <packages.txt; [ -f requirements.txt ] && pip3 install --user -r requirements.txt; pip3 install --user streamlit; echo '✅ Packages installed and Requirements met'",
  "postAttachCommand":
    "server": "recorredor_run_reco.py 
      "app.py"

reparar_cat: /mount/admin/install_path: No such file or directory.py
