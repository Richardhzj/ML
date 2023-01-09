from polygon import Polygon
from vector2d import Vector2D
from checkIntersect import do_intersect
import math


class Environment:
    def __init__(self, filename):
        self.width = 800
        self.height = 600
        self.start = Vector2D(0, 0)
        self.goal = Vector2D(800, 600)
        self.obstacles = []

        self.obstacles_lines = {}

        f = open(filename, 'r')
        envtxt = f.readlines()
        f.close()
        polygonstxt, *resttxt = envtxt
        polygons = int(polygonstxt)

        for polygon_number in range(polygons):
            ntxt, *resttxt = resttxt
            n = int(ntxt)
            p = Polygon(n)
            for line in resttxt[:n]:
                [x, y] = [float(x) for x in line.split()]
                p.vertices.append(Vector2D(x, y))
            resttxt = resttxt[n:]

            self.obstacles.append(p)

            # extra codes
            # get all the existed sides of polygons
            for original_v in p.vertices:
                if p.vertices.index(original_v) + 1 == len(p.vertices):
                    next_vertex = p.vertices[0]
                else:
                    next_vertex = p.vertices[p.vertices.index(original_v) + 1]
                side_of_polygon = math.sqrt((original_v.x - next_vertex.x) ** 2 + (original_v.y - next_vertex.y) ** 2)
                self.obstacles_lines[(original_v, next_vertex)] = 1

            #     distance_of_polygon = []
            #     print("origin points:")
            #     print((v.x, v.y))
            #     for targetV in p.vertices:
            #         if v.x == targetV.x and v.y == targetV.y:
            #             continue
            #         print("target point: ")
            #         print((targetV.x, targetV.y))
            #         # get all lines from one vertex in a polygon这里不该判断， 因为要把最短的两条取出来，不然把更长的取了
            #         dis_of_vertexes_in_one_poly = math.sqrt((v.x - targetV.x) ** 2 + (v.y - targetV.y) ** 2)
            #         distance_of_polygon.append(dis_of_vertexes_in_one_poly)
            #         print("distance: ", str(dis_of_vertexes_in_one_poly), " x: " + str(targetV.x), " y: "+ str(targetV.y))
            #         # key: len of line value: (Vector2D,Vector2D)
            #         # insert new line into the dict
            #         computed_line_with_len[dis_of_vertexes_in_one_poly] = (v, targetV)
            #         # print(computed_line_with_len)
            #     # print("len of lines " + str(len(computed_line_with_len)))
            #     # get the shortest two lines of the vertex, these are the sides of the polygon
            #     for key in computed_line_with_len:
            #         print("distance for one vertex", str(key))
            #     distance_of_polygon.sort()
            #     line1_of_polygon = distance_of_polygon[0]
            #     line2_of_polygon = distance_of_polygon[1]
            #     print(line1_of_polygon,line2_of_polygon)
            #     # todo 取完后， 再判断说针对每个点，取出的两条线是否反过来的vertex已经放进去了
            #     # for each vertex, check if the two shortest lines have been set into the dict
            #
            #     if (computed_line_with_len[line1_of_polygon][0],
            #         computed_line_with_len[line1_of_polygon][1]) not in self.obstacles_lines and (
            #             computed_line_with_len[line1_of_polygon][1],
            #             computed_line_with_len[line1_of_polygon][0]) not in self.obstacles_lines:
            #         # cause we only need the coords of two vertexes which are in the key
            #         self.obstacles_lines[computed_line_with_len[line1_of_polygon]] = 1
            #         testLines += 1
            #         print("line1 -- " + str(line1_of_polygon))
            #     if (computed_line_with_len[line2_of_polygon][0],
            #         computed_line_with_len[line2_of_polygon][1]) not in self.obstacles_lines and (
            #             computed_line_with_len[line2_of_polygon][1],
            #             computed_line_with_len[line2_of_polygon][0]) not in self.obstacles_lines:
            #         self.obstacles_lines[computed_line_with_len[line2_of_polygon]] = 1
            #         print("line2 -- " + str(line2_of_polygon))
            #         testLines += 1
            #     print("lines in a polygon " + str(testLines))
            #     print("--------------------------------------------")
            # print(len(computed_line_with_len))
            # print("zzz")
            # print(len(self.obstacles_lines))
            # # get the two nearest line, they are the sides of the polygon which is the obstacles.
            #


    @staticmethod
    def printPath(searchName, path):
        with open('output/' + searchName + '.js', 'w') as f:
            f.write('window.' + searchName + ' =\n\t[\n')
            for v in path:
                f.write('\t\t[{}, {}],\n'.format(v.x, v.y))
            f.write('\t];\n')

