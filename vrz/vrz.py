from typer import Typer

def main():
    app = Typer(no_args_is_help=True)

    @app.command()
    def minor():
        # poetry version minor
        print(f"Hello!")

    @app.command()
    def latest():
        # poetry version -s
        print(f"Hello!")

    app()

if __name__ == "__main__":
    main()