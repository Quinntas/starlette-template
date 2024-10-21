from src.core.context import Context
from src.core.responses import json_response
from src.modules.user.commands.create_user.create_user_command import create_user_command
from src.modules.user.commands.create_user.create_user_dto import CreateUserDTO


async def create_user_controller(ctx: Context):
    body = await ctx.request.json()

    dto = CreateUserDTO(
        email=body['email'],
        password=body['password']
    )

    try:
        await create_user_command(dto)
    except Exception as e:
        return json_response(ctx, 400, {"message": str(e)})

    return json_response(ctx, 201, {"message": "User created successfully"})
