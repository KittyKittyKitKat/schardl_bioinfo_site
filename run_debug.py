# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
from bioinfo_site import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
