'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
# Use the following method to import the internal module in the current same directory


'''
Replace the ModuleName with any name you'd like
'''
class ModuleName(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="back",
        description="回"
    )
    module_group: interactions.SlashCommand = module_base.group(
        name="to",
        description="到"
    )

    @module_group.subcommand("top", sub_cmd_description="回到顶楼")
    
    async def module_group_ping(self, ctx: interactions.SlashContext):
        channel=ctx.channel
        try:
            mess=await channel.fetch_message(message_id=channel.last_message_id)
        
            elev=mess.jump_url.rsplit('/', 1)[0]+'/0'
            
            await ctx.send(content=elev)
        except:
            await ctx.send(content='再试一次!')
        
