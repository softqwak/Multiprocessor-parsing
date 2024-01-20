# LOMONOSOV
parsing

## PARSER OPTIONS
```json
{
    "set": "number of tasks that will be executed asynchronously",
    "users": [
        "user IDs"
    ]
}
```

## PARSER INSTRUCTIONS

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
            "main": null
        },
        ...
        {
            "descript": "options_read",
            "date_format": "%H:%M %d.%m.%Y"
        }
    ],
    "keywords": {
        
    }
}
```