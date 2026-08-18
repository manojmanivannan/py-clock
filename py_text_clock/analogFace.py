import math
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class AnalogClock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.radius_y = 7
        self.radius_x = 14
        self.center_y = 7
        self.center_x = 15
        self.grid_h = 15
        self.grid_w = 31

    def _draw_line(self, grid, x0, y0, x1, y1, char):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            if 0 <= y0 < self.grid_h and 0 <= x0 < self.grid_w:
                if grid[y0][x0] == ' ':
                    grid[y0][x0] = char
            
            if x0 == x1 and y0 == y1:
                break
            
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def generate_panel(self) -> Panel:
        grid = [[' ' for _ in range(self.grid_w)] for _ in range(self.grid_h)]
        
        # Place numbers
        for i in range(1, 13):
            angle = i * 30 * math.pi / 180
            y = int(round(self.center_y - self.radius_y * math.cos(angle)))
            x = int(round(self.center_x + self.radius_x * math.sin(angle)))
            
            num_str = str(i)
            if i >= 10:
                if x > 0:
                    x -= 1 # adjust for two digit numbers to center them
            
            if 0 <= y < self.grid_h and 0 <= x < self.grid_w:
                for j, ch in enumerate(num_str):
                    if 0 <= x+j < self.grid_w:
                        grid[y][x+j] = ch

        # Calculate hand angles
        sec_angle = self.second * 6 * math.pi / 180
        min_angle = (self.minute + self.second / 60.0) * 6 * math.pi / 180
        hr_angle = ((self.hour % 12) + self.minute / 60.0) * 30 * math.pi / 180

        # Draw hands
        # Hour hand (shorter)
        h_len_y = int(self.radius_y * 0.5)
        h_len_x = int(self.radius_x * 0.5)
        h_y = int(round(self.center_y - h_len_y * math.cos(hr_angle)))
        h_x = int(round(self.center_x + h_len_x * math.sin(hr_angle)))
        self._draw_line(grid, self.center_x, self.center_y, h_x, h_y, 'H')

        # Minute hand (longer)
        m_len_y = int(self.radius_y * 0.75)
        m_len_x = int(self.radius_x * 0.75)
        m_y = int(round(self.center_y - m_len_y * math.cos(min_angle)))
        m_x = int(round(self.center_x + m_len_x * math.sin(min_angle)))
        self._draw_line(grid, self.center_x, self.center_y, m_x, m_y, 'M')

        # Second hand (longest)
        s_len_y = int(self.radius_y * 0.9)
        s_len_x = int(self.radius_x * 0.9)
        s_y = int(round(self.center_y - s_len_y * math.cos(sec_angle)))
        s_x = int(round(self.center_x + s_len_x * math.sin(sec_angle)))
        self._draw_line(grid, self.center_x, self.center_y, s_x, s_y, '.')

        # Center point
        grid[self.center_y][self.center_x] = 'O'

        # Construct rich text
        rt = Text()
        for y in range(self.grid_h):
            for x in range(self.grid_w):
                char = grid[y][x]
                if char in ('H', 'M'):
                    rt.append(char, style="bold cyan")
                elif char == '.':
                    rt.append(char, style="red")
                elif char == 'O':
                    rt.append(char, style="bold yellow")
                elif char != ' ':
                    rt.append(char, style="bold green")
                else:
                    rt.append(' ')
            if y < self.grid_h - 1:
                rt.append('\n')

        return Panel(rt, title="Analog Clock", expand=False, border_style="blue")

    def show(self):
        console = Console()
        console.print(self.generate_panel())
