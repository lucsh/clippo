if [[ "$1" == "train" ]]; then
  echo "Installing local dependencies..."
  # make sure you have the last pip to avoid tensorflow installation issues
  python3.6 -m pip install --upgrade pip --user
  python3.6 -m pip install --upgrade --user -r requirements.txt

  echo "training ..."
  rasa train
fi

echo "Copying actions..."
cp actions.py install/rasa/actions/
cp .env install/rasa/actions/

echo "Copying models..."
cp models/* install/rasa/models/

echo "Building custom image..."
cd install || exit
docker build -t rasa-clippo .

if [ ! -f rasa/.env ]
then
     echo "File install/rasa/.env not found. Please create one based on install/rasa/example.env"
     exit
fi

echo "Copying to rasa directory to /etc ..."
sudo rm -rf /etc/rasa
sudo cp -avr rasa /etc/

echo "Setting permisions and group ..."
sudo chgrp -R root /etc/rasa/* && sudo chmod -R 770 /etc/rasa/*
sudo chown -R 1001 /etc/rasa/db && sudo chmod -R 750 /etc/rasa/db

echo 'Running docker-compose'
cd /etc/rasa || exit
#docker-compose down
docker-compose up -d

echo 'Remember to setup you password'
echo '***'
echo '* docker-compose exec rasa-x bash -c "python3 /app/scripts/manage_users.py create me <PASSWORD> admin --update" '
echo '***'
echo 'Then, navigate to the hostname or IP where your server is reachable and log in using your newly created password.'
