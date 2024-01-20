# Lomonosov
parsing vk, telegram, web

## Parser options

```json
{
    "set": "number of tasks that will be executed asynchronously",
    "users": [
        "user IDs"
    ]
}
```

## Parser instruction

```json
{
    "search": {
        "descript": "urls",
        "absolute_path": false,
        "premain": {
            "teg": "teg",
            "classes": [
                "class"
            ],
            "id": "id"
        },
        "main": {
            "teg": "teg",
            "classes": [
                "class"
            ],
            "id": "id"
        }
    },
    "read": [
        {
            "descript": "title",
            "premain": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            },
            "main": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            }
        },
        {
            "descript": "text",
            "premain": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            },
            "main": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            }
        },
        {
            "descript": "any content",
            "premain": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            },
            "main": {
                "teg": "teg",
                "classes": [
                    "class"
                ],
                "id": "id"
            }
        },
        {
            "descript": "options_read",
            "date_format": "%H:%M %d.%m.%Y"
        }
    ],
    "keywords": {
        
    }
}
```