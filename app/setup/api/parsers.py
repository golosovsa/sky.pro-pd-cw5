"""
    App request arguments parsers
"""

from flask_restx.reqparse import RequestParser  # type: ignore

create_unit_args_parser: RequestParser = RequestParser()

create_unit_args_parser.add_argument(
    name="name",
    type=str,
    location="form",
    required=True,
    help="Unit name",
)

create_unit_args_parser.add_argument(
    name="unit_class",
    type=str,
    location="form",
    required=True,
    help="Unit class name",
)

create_unit_args_parser.add_argument(
    name="weapon",
    type=str,
    location="form",
    required=True,
    help="Weapon name",
)

create_unit_args_parser.add_argument(
    name="armor",
    type=str,
    location="form",
    required=True,
    help="Armor name",
)
