HOST='pdb2json.samireland.com'

ssh $HOST "rm -r ~/$HOST/source/*"

scp pdb2json.py $HOST:~/$HOST/source/
scp requirements.txt $HOST:~/$HOST/source/

ssh samireland.com "sed -i s/'DEBUG = True'/'DEBUG = False'/g ~/$HOST/source/pdb2json.py"
ssh samireland.com "sed -i s/'ALLOWED_HOSTS = \[\]'/'ALLOWED_HOSTS = \[£pdb2json.samireland.com£]'/g ~/$HOST/source/pdb2json.py"
ssh samireland.com "sed -i s/£/\'/g ~/$HOST/source/pdb2json.py"

ssh samireland.com "~/$HOST/env/bin/pip install -r ~/$HOST/source/requirements.txt"
