from . import cnx


def main():
    # Start with `python -m swagger_server` 
    cnx.run(port=3000)


if __name__ == '__main__':
    main()
