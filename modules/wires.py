import random
import enum
import modules

class Wires(modules.Module):
    identifiers = ['wires']
    display_name = "Wires"
    manual_name = "Wires"
    help_text = "`{cmd} cut 3` to cut the third wire. Empty spaces are not counted."
    module_score = 1
    vanilla = True

    @enum.unique
    class Color(enum.Enum):
        black =  "#000"
        blue =   "#00f"
        red =    "#f00"
        white =  "#fff"
        yellow = "#ff0"

    PATHS_UNCUT = [
        "M65.898438,90.912109 c -1.576082,-0.198603 -3.215872,-0.156976 -4.921876,0.208985 l 1.259766,5.867187 c 4.023083,-0.863006 8.043492,1.43865 12.857422,4.818359 4.81393,3.37971 10.054968,7.72643 16.78125,8.39844 25.11869,2.50953 49.92935,-2.81228 73.95508,-1.40039 4.85979,0.28558 9.41352,3.04832 14.34375,6.45117 4.93022,3.40285 10.13574,7.40432 16.6289,8.98828 25.2538,6.16046 51.03948,9.12443 76.47266,12.75195 l 0.8457,-5.93945 c -25.54045,-3.64283 -51.1276,-6.59845 -75.89648,-12.64062 -4.88126,-1.19075 -9.58377,-4.60606 -14.64258,-8.09766 -5.05881,-3.4916 -10.57237,-7.1007 -17.40039,-7.50195 -25.1198,-1.47619 -49.84318,3.80252 -73.710937,1.41797 -4.31262,-0.43087 -8.931655,-3.82893 -13.929687,-7.337896 -3.748525,-2.631722 -7.914333,-5.388564 -12.642578,-5.984375 z",
        "M79.429688,124.41211 c -5.156519,-0.0461 -10.27896,0.83644 -15.304688,3.12109 l 2.484375,5.46289 c 11.067282,-5.03109 23.279695,-1.92804 36.576175,2.85547 13.29647,4.78351 27.308,11.21787 41.6914,11.05078 24.59358,-0.28569 49.50733,-7.64146 70.92969,-0.16796 8.77888,3.06263 19.72486,10.66295 30.37109,15.88281 5.32312,2.60993 10.6214,4.6592 15.86915,5.07226 5.24774,0.41307 10.56094,-1.05509 14.71289,-5.20703 l -4.24415,-4.24219 c -2.93547,2.93548 -6.02885,3.77923 -9.99804,3.4668 -3.96919,-0.31243 -8.69755,-2.0252 -13.69727,-4.47656 -9.99943,-4.90273 -20.88848,-12.61966 -31.03711,-16.16016 -23.86911,-8.32707 -49.60292,-0.43946 -72.97461,-0.16797 -12.49367,0.14514 -25.98731,-5.80099 -39.59179,-10.69531 -8.502802,-3.05895 -17.192915,-5.7181 -25.787112,-5.79492 z",
        "M93.236328,154.05859 c -3.682182,-0.001 -7.367143,0.58118 -10.96289,1.36524 -7.191495,1.56812 -14.218755,3.95004 -20.587891,4.78515 l 0.78125,5.94922 c 7.225121,-0.94734 14.364494,-3.40742 21.085937,-4.87304 6.721444,-1.46563 12.831094,-1.92708 18.244146,0.41796 1.31363,0.5691 2.40433,1.74556 3.45117,3.62305 1.04683,1.87749 1.94737,4.3451 2.90625,6.89063 0.95887,2.54552 1.9636,5.17601 3.5664,7.48632 1.60281,2.31032 4.0819,4.35726 7.32813,4.79493 30.95881,4.17391 62.07066,-1.60513 92.36133,-4.2168 20.80879,-1.79414 42.25766,8.00586 65.10937,8.00586 v -6 c -21.0513,0 -42.69307,-9.96157 -65.625,-7.98438 -30.68385,2.64557 -61.35175,8.25328 -91.04492,4.25 -1.36836,-0.18448 -2.18586,-0.80885 -3.19922,-2.26953 -1.01336,-1.46068 -1.9467,-3.70174 -2.88086,-6.18164 -0.93415,-2.47989 -1.8829,-5.18933 -3.28125,-7.69726 -1.39835,-2.50793 -3.34766,-4.92514 -6.30664,-6.20703 -3.58386,-1.55261 -7.263129,-2.13736 -10.945312,-2.13868 z",
        "M93.806641,183.77734 c -11.315125,-0.13224 -22.4792,2.98695 -32.875,3.68946 l 0.404297,5.98632 c 14.959168,-1.01088 29.473876,-5.75563 42.312502,-2.4414 10.53733,2.72017 20.92191,9.49114 33.33594,10.89258 22.6526,2.55729 45.40177,2.42578 66.89843,7.46484 11.72512,2.7485 21.48797,5.87484 29.72657,6.19141 7.52568,0.28916 14.95175,-1.70331 21.84765,-2.86328 6.8959,-1.15998 13.04955,-1.49331 18.30859,1.13867 l 2.68555,-5.36524 c -7.08388,-3.54524 -14.72832,-2.91099 -21.99023,-1.68945 -7.26192,1.22154 -14.35456,3.02399 -20.6211,2.7832 -6.82274,-0.26216 -16.62776,-3.23351 -28.58789,-6.03711 -22.42372,-5.25637 -45.42207,-5.08076 -67.5957,-7.58398 -10.54186,-1.19009 -20.67671,-7.68608 -32.50781,-10.74024 -3.78262,-0.97646 -7.570091,-1.3817 -11.341799,-1.42578 z",
        "M101.34375,222.14453 c -11.915491,-0.38005 -23.809415,0.33728 -35.582031,2.51758 l 1.091797,5.90039 c 45.161684,-8.36397 93.271904,5.7762 137.707034,20.58594 3.03639,1.01199 6.09504,0.48029 8.61523,-0.68164 2.52019,-1.16194 4.68543,-2.87707 6.76367,-4.58594 4.15649,-3.41774 7.98075,-6.57535 11.18555,-6.8125 13.57108,-1.00422 27.7339,2.83008 42.57227,2.83008 v -6 c -13.75374,0 -28.07255,-3.91824 -43.01563,-2.8125 -6.16408,0.45613 -10.58272,4.89575 -14.55273,8.16015 -1.98501,1.63221 -3.85206,3.02986 -5.46485,3.77344 -1.61279,0.74358 -2.78716,0.91073 -4.20703,0.4375 -33.42928,-11.14161 -69.36681,-22.17235 -105.11328,-23.3125 z",
        "M135.9082,249.06641 c -6.63407,0 -12.00903,3.43897 -16.78711,7.08007 -4.77807,3.64111 -9.16866,7.58585 -13.63281,9.65821 -6.384118,2.96364 -15.125811,4.48388 -23.103514,3.75 -7.977704,-0.73388 -15.011192,-3.66727 -18.826172,-8.90821 l -4.84961,3.53125 c 5.213707,7.16248 14.032238,10.51493 23.126954,11.35157 9.094715,0.83663 18.646612,-0.7871 26.177732,-4.28321 5.65903,-2.62704 10.26447,-6.91246 14.74414,-10.32617 4.47968,-3.41371 8.62368,-5.85351 13.15039,-5.85351 8.76005,0 17.68419,1.37193 25.71875,4.49609 0.64279,0.24994 1.23113,0.84192 1.88086,2.14844 0.64974,1.30651 1.21441,3.16606 1.81641,5.125 0.602,1.95894 1.22072,4.02182 2.39844,5.91992 1.17771,1.8981 3.32051,3.72029 6.04296,3.93359 33.00535,2.58612 66.99569,0.93388 99.24805,-7.13672 l -1.45508,-5.82031 c -31.47542,7.87618 -64.83765,9.52008 -97.32421,6.97461 -0.6586,-0.0516 -0.82751,-0.17109 -1.41211,-1.11328 -0.58461,-0.94219 -1.17963,-2.61903 -1.76368,-4.51953 -0.58404,-1.9005 -1.17719,-4.01931 -2.17968,-6.03516 -1.00249,-2.01585 -2.56005,-4.08924 -5.07813,-5.06836 -8.87528,-3.45106 -18.5094,-4.90429 -27.89258,-4.90429 z",
    ]

    PATHS_CUT = [
        "M65.898438,90.912109 c -1.576082,-0.198603 -3.215871,-0.156976 -4.921876,0.208985 l 1.259766,5.867187 c 4.023083,-0.863006 8.043492,1.43865 12.857422,4.818359 4.81393,3.37971 10.054967,7.72644 16.78125,8.39844 25.11869,2.50954 49.92935,-2.81228 73.95508,-1.40039 l 0.35156,-5.98828 c -25.11979,-1.47618 -49.84318,3.80253 -73.710937,1.41797 -4.312619,-0.43086 -8.931655,-3.82893 -13.929687,-7.337896 -3.748525,-2.631722 -7.914333,-5.388564 -12.642578,-5.984375 z m 132.326172,27.503911 -1.42188,5.82812 c 25.2538,6.16048 51.03948,9.12442 76.47266,12.75195 l 0.8457,-5.93945 c -25.54045,-3.64283 -51.1276,-6.59844 -75.89648,-12.64062 z",
        "M79.429688,124.41211 c -5.156519,-0.0461 -10.27896,0.83644 -15.304688,3.12109 l 2.484375,5.46289 c 11.067282,-5.03109 23.279695,-1.92804 36.576175,2.85547 13.29647,4.78351 27.30801,11.21787 41.6914,11.05078 l -0.0684,-6 c -12.49367,0.14514 -25.98732,-5.80099 -39.59179,-10.69531 -8.502802,-3.05895 -17.192915,-5.7181 -25.787112,-5.79492 z m 109.509762,12.98047 c -3.24251,0.10601 -6.48805,0.32684 -9.72265,0.60547 -2.02254,0.17421 -4.04115,0.37206 -6.05664,0.58007 l 0.61523,5.96876 c 1.9942,-0.20583 3.98071,-0.40009 5.95703,-0.57032 12.64292,-1.08905 24.82164,-1.1678 36.07422,2.75782 8.77888,3.06263 19.72485,10.66295 30.37109,15.88281 5.32312,2.60993 10.6214,4.6592 15.86915,5.07226 5.24774,0.41307 10.56094,-1.05509 14.71289,-5.20703 l -4.24415,-4.24219 c -2.93547,2.93548 -6.02885,3.77923 -9.99804,3.4668 -3.96919,-0.31243 -8.69755,-2.0252 -13.69727,-4.47656 -9.99943,-4.90273 -20.88848,-12.61967 -31.03711,-16.16016 -9.40334,-3.28048 -19.11621,-3.99575 -28.84375,-3.67773 z",
        "M93.236328,154.05859 c -3.682182,-0.001 -7.367143,0.58118 -10.96289,1.36524 -7.191495,1.56812 -14.218755,3.95004 -20.587891,4.78515 l 0.78125,5.94922 c 7.22512,-0.94734 14.364494,-3.40742 21.085937,-4.87304 6.721444,-1.46563 12.831095,-1.92708 18.244146,0.41796 1.31363,0.5691 2.40433,1.74556 3.45117,3.62305 1.04683,1.87749 1.94737,4.3451 2.90625,6.89063 0.95887,2.54552 1.9636,5.17601 3.5664,7.48632 1.60281,2.31032 4.0819,4.35727 7.32813,4.79493 18.32191,2.47018 36.70066,1.43401 54.92578,-0.34375 l -0.58203,-5.97071 c -18.05916,1.76158 -35.97008,2.73834 -53.54297,0.36914 -1.36836,-0.18448 -2.18586,-0.80885 -3.19922,-2.26953 -1.01336,-1.46068 -1.9467,-3.70174 -2.88086,-6.18164 -0.93415,-2.4799 -1.8829,-5.18933 -3.28125,-7.69726 -1.39835,-2.50793 -3.34766,-4.92514 -6.30664,-6.20703 -3.58386,-1.55261 -7.26313,-2.13736 -10.945312,-2.13868 z m 126.199222,20.01953 c -2.82755,-0.0831 -5.67453,-0.0225 -8.54102,0.22461 l 0.51563,5.97852 c 20.80879,-1.79414 42.25766,8.00586 65.10937,8.00586 v -6 c -18.41989,0 -37.29117,-7.62698 -57.08398,-8.20899 z",
        "M93.806641,183.77734 c -11.315126,-0.13224 -22.479199,2.98694 -32.875,3.68946 l 0.404297,5.98632 c 14.959167,-1.01089 29.473874,-5.75564 42.312502,-2.4414 l 1.5,-5.8086 c -3.78262,-0.97646 -7.570091,-1.38169 -11.341799,-1.42578 z m 43.849609,12.16602 -0.67187,5.96094 c 22.6526,2.55729 45.40177,2.42578 66.89843,7.46484 11.72513,2.74851 21.48797,5.87483 29.72657,6.19141 7.52568,0.28916 14.95175,-1.70331 21.84765,-2.86328 6.8959,-1.15998 13.04955,-1.49331 18.30859,1.13867 l 2.68555,-5.36524 c -7.08387,-3.54524 -14.72832,-2.91099 -21.99023,-1.68945 -7.26192,1.22154 -14.35456,3.02399 -20.6211,2.7832 -6.82274,-0.26216 -16.62775,-3.23351 -28.58789,-6.03711 -22.42372,-5.25637 -45.42207,-5.08076 -67.5957,-7.58398 z",
        "M101.34375,222.14453 c -11.915491,-0.38005 -23.809414,0.33729 -35.582031,2.51758 l 1.091797,5.90039 c 45.161694,-8.36396 93.271904,5.7762 137.707034,20.58594 l 1.89648,-5.69141 c -33.42928,-11.14161 -69.36681,-22.17235 -105.11328,-23.3125 z m 140.42969,10.91406 c -3.65876,-0.21192 -7.35603,-0.24909 -11.0918,0.0273 l 0.44336,5.98242 c 13.57108,-1.00421 27.7339,2.83008 42.57227,2.83008 v -6 c -10.3153,0 -20.94756,-2.20408 -31.92383,-2.83985 z",
        "M135.9082,249.06641 c -6.63407,0 -12.00903,3.43897 -16.78711,7.08007 -4.77807,3.64111 -9.16867,7.58585 -13.63281,9.65821 -6.384119,2.96364 -15.125811,4.48387 -23.103514,3.75 -7.977704,-0.73388 -15.011192,-3.66727 -18.826172,-8.90821 l -4.84961,3.53125 c 5.213707,7.16248 14.032238,10.51493 23.126954,11.35157 9.094715,0.83663 18.646612,-0.7871 26.177732,-4.28321 5.65903,-2.62704 10.26447,-6.91246 14.74414,-10.32617 4.47968,-3.41371 8.62368,-5.85351 13.15039,-5.85351 z m 27.89258,4.90429 -2.17383,5.5918 c 0.64279,0.24994 1.23113,0.84192 1.88086,2.14844 0.64974,1.30651 1.21441,3.16606 1.81641,5.125 0.602,1.95894 1.22072,4.02182 2.39844,5.91992 1.17771,1.8981 3.32051,3.72029 6.04296,3.93359 33.00536,2.58613 66.99569,0.93388 99.24805,-7.13672 l -1.45508,-5.82031 c -31.47542,7.87618 -64.83765,9.52009 -97.32421,6.97461 -0.6586,-0.0516 -0.82751,-0.17109 -1.41211,-1.11328 -0.58461,-0.94219 -1.17963,-2.61903 -1.76368,-4.51953 -0.58404,-1.9005 -1.17719,-4.01931 -2.17968,-6.03516 -1.0025,-2.01585 -2.56005,-4.08925 -5.07813,-5.06836 z",
    ]

    def __init__(self, bomb, ident):
        super().__init__(bomb, ident)
        wire_count = random.randint(3, 8)
        if wire_count > 6: wire_count = 6
        self.positions = sorted(random.sample(range(6), wire_count))
        self.cut = [False] * wire_count
        self.colors = []
        for _ in range(wire_count):
            self.colors.append(random.choice(list(Wires.Color)))
        self.log(f"There are {len(self.colors)} wires: {' '.join(color.name for color in self.colors)}")

    def get_svg(self, led):
        svg = (
            f'<svg viewBox="0 0 348 348" fill="#fff" stroke="none" stroke-width="2" stroke-linecap="butt" stroke-linejoin="round" stroke-miterlimit="10">'
            f'<path stroke="#000" d="M5 5h338v338h-338zM47 62h30v226h-30zM258 107h30v178h-30z"/>'
            f'<circle fill="{led}" stroke="#000" cx="298" cy="40.5" r="15" stroke-width="2"/>')
        for pos, color, cut in zip(self.positions, self.colors, self.cut):
            paths = Wires.PATHS_CUT if cut else Wires.PATHS_UNCUT
            svg += f'<path fill="{color.value}" stroke="#000" d="{paths[pos]}" />'
        svg += '</svg>'
        return svg

    @modules.check_solve_cmd
    async def cmd_cut(self, author, parts):
        if len(parts) != 1 or not parts[0].isdigit():
            await self.usage(author)
        elif parts[0] == "0":
            await self.bomb.channel.send(f"{author.mention} Arrays start at 0, but wires start at 1.")
        else:
            wire = int(parts[0]) - 1
            if wire not in range(len(self.colors)):
                await self.bomb.channel.send(f"There are only {len(self.colors)} wires. How on earth am I supposed to cut wire {parts[0]}?")
            else:
                expected = self.get_solution()
                self.log(f"player cut wire {wire+1}. expected wire {expected+1}")
                self.cut[wire] = True
                if expected == wire:
                    await self.handle_solve(author)
                else:
                    await self.handle_strike(author)

    def get_solution(self):
        def count(color):
            return self.colors.count(color)

        def first(color):
            return self.colors.index(color)

        def last(color):
            return len(self.colors) - 1 - self.colors[::-1].index(color)

        serial_odd = int(self.bomb.serial[-1]) % 2 == 1
        self.log('the last digit of the serial number is {:s}'.format('odd' if serial_odd else 'even'))

        if len(self.colors) == 3:
            if count(Wires.Color.red) == 0:
                self.log('rule: there are no red wires')
                return 1
            elif self.colors[-1] == Wires.Color.white:
                self.log('rule: the last wire is white')
                return 2
            elif count(Wires.Color.blue) > 1:
                self.log('rule: there is more than one blue wire')
                return last(Wires.Color.blue)
            else:
                self.log('rule: wildcard')
                return 2
        elif len(self.colors) == 4:
            if count(Wires.Color.red) > 1 and serial_odd:
                self.log('rule: there is more than one red wire')
                return last(Wires.Color.red)
            elif self.colors[-1] == Wires.Color.yellow and count(Wires.Color.red) == 0:
                self.log('rule: the last wire is yellow and there are no red wires')
                return 0
            elif count(Wires.Color.blue) == 1:
                self.log('rule: there is exactly one blue wire')
                return 0
            elif count(Wires.Color.yellow) > 1:
                self.log('rule: there is more than one yellow wire')
                return 3
            else:
                self.log('rule: wildcard')
                return 1
        elif len(self.colors) == 5:
            if self.colors[-1] == Wires.Color.black and serial_odd:
                self.log('rule: the last wire is black and the last digit of the serial number is odd')
                return 3
            elif count(Wires.Color.red) == 1 and count(Wires.Color.yellow) > 1:
                self.log('rule: there is exactly one red wire and there is more than one yellow wire')
                return 0
            elif count(Wires.Color.black) == 0:
                self.log('rule: there are no black wires')
                return 1
            else:
                self.log('rule: wildcard')
                return 0
        else:
            if count(Wires.Color.yellow) == 0 and serial_odd:
                self.log('rule: there are no yellow wires and the last digit of the serial number is odd')
                return 2
            elif count(Wires.Color.yellow) == 1 and count(Wires.Color.white) > 1:
                self.log('rule: there is exactly one yellow wire and there is more than one white wire')
                return 3
            elif count(Wires.Color.red) == 0:
                self.log('rule: there are no red wires')
                return 5
            else:
                self.log('rule: wildcard')
                return 3

    COMMANDS = {
        "cut": cmd_cut
    }
