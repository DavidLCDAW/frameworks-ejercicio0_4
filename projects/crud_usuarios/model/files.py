from model.User import User


def write(formato: str, users: list[User]):
    if formato == "json":
        filename = "user.json"
        user_json = [user.to_json() for user in users]
        content = "[\n" + ",\n".join(user_json) + "\n]"
    elif formato == "csv":
        filename = "user.csv"
        content = ""
        if users:
            content = users[0].to_csv(write_header=True)
            for user in users[1:]:
                content += user.to_csv(write_header=False)
    elif formato == "toml":
        filename = "user.toml"
        user_toml = [user.to_toml() for user in users]
        content = "\n".join(user_toml)
    elif formato == "yaml":
        filename = "user.yaml"
        user_yaml = [user.to_yaml() for user in users]
        content = "\n".join(user_yaml)
    else:
        raise ValueError(f"Formato no soportado: {formato}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
