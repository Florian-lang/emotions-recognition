#!/bin/bash

HOOKS_PATH=".git/hooks/pre-commit"

echo "#!/bin/sh" > $HOOKS_PATH
echo "python3 -m flake8 ." >> $HOOKS_PATH

chmod +x $HOOKS_PATH

echo "Hook de pre-commit créé."
