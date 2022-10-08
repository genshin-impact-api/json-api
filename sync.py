if __name__ == "__main__":
    with open("db.json", "w") as data_file:
        data_file.write(
            """
            {
                "posts": [
                    {
                        "id": 1,
                        "title": "hello"
                    }
                ],
                "profile": {
                    "name": "typicode"
                }
            }
            """
        )
