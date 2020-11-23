from enum import Enum


class Constant:
    ROLE = {
        'USER_ROLE': Enum(
            value='USER_ROLE',
            names=[
                ('user', 'user'),
                ('admin', 'admin')
            ]
        )
    }
