<!-- GETTING STARTED -->
## Getting Started
Django testing for Imagine apps.

### Prerequisites

* docker

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Vidanilo10/testing_imagine_apps.git
   ```
3. Run project
   ```sh
    docker-compose run django python manage.py loaddata data.json
    docker-compose up
    ```
4. Go to localhost:
   http://localhost:8000/app1/api/v1/testing-model/