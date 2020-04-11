import unittest
from Graph import Graph, quickest_route, generate_edges


class TestProject8(unittest.TestCase):

    def test_insert_edge(self):
        stu = Graph()
        stu.add_to_graph(2, 1, 6)
        stu.add_to_graph(3)

        assert len(stu.adj_map) == 3
        assert stu.size == 3

        edge = stu.get_vertex(2).edges[1]

        assert len(stu.get_vertex(2).edges) == 1
        assert edge.get_start() == 2
        assert edge.get_destination() == 1
        assert edge.get_weight() == 6
        
        edge = stu.get_vertex(1).edges[2]
        assert len(stu.get_vertex(2).edges) == 1
        assert edge.get_start() == 1
        assert edge.get_destination() == 2
        assert edge.get_weight() == 6

        assert len(stu.get_vertex(3).edges) == 0


    def test_construct_graph_from_file(self):
        stu = Graph()
        stu.construct_graph_from_file("smallSampleGraph.txt")
        assert len(stu.adj_map) == 6
        assert stu.size == 6

        edge = stu.get_vertex("EmpireState").edges
        assert len(edge) == 3
        assert edge["UnitedNations"].get_start() == "EmpireState"
        assert edge["UnitedNations"].get_destination() == "UnitedNations"
        assert edge["UnitedNations"].get_weight() == 2
        assert edge["TimesSquare"].get_start() == "EmpireState"
        assert edge["TimesSquare"].get_destination() == "TimesSquare"
        assert edge["TimesSquare"].get_weight() == 1
        assert edge["MidtownWest"].get_start() == "EmpireState"
        assert edge["MidtownWest"].get_destination() == "MidtownWest"
        assert edge["MidtownWest"].get_weight() == 2

        assert len(stu.get_vertex("LincolnCenter").edges) == 3
        assert len(stu.get_vertex("CentralPark").edges) == 3
        assert len(stu.get_vertex("UnitedNations").edges) == 3
        assert len(stu.get_vertex("MidtownWest").edges) == 3
        assert len(stu.get_vertex("TimesSquare").edges) == 5

    def test_bfs(self):
        stu = Graph()
        stu.add_to_graph("A", "D", 0)
        stu.add_to_graph("A", "B", 0)
        stu.add_to_graph("B", "E", 0)
        stu.add_to_graph("B", "F", 0)
        stu.add_to_graph("E", "F", 0)
        stu.add_to_graph("F", "C", 0)

        possible_paths = [["A", "B", "F", "C"], ["A", "B", "E", "F", "C"]]
        stu_path = stu.bfs("A", "C",[])
        print("Your path: ", stu_path)
        assert stu_path in possible_paths

    def test_dfs(self):
        stu = Graph()
        stu.add_to_graph("A", "D", 0)
        stu.add_to_graph("A", "B", 0)
        stu.add_to_graph("B", "E", 0)
        stu.add_to_graph("B", "F", 0)
        stu.add_to_graph("E", "F", 0)
        stu.add_to_graph("F", "C", 0)

        possible_paths = [["A", "B", "F", "C"], ["A", "B", "E", "F", "C"]]
        stu_path = stu.dfs("A", "C", [])
        print("Your path: ", stu_path)
        assert stu_path in possible_paths

    def test_quickest_route(self):
        stu = quickest_route("smallSampleGraph.txt", "LincolnCenter", "LincolnCenter")
        print("Your shortest path: ", stu)
        assert stu == [0, "LincolnCenter"]

        stu = quickest_route("smallSampleGraph.txt", "LincolnCenter", "Manhattan")
        print("Your shortest path: ", stu)
        assert stu == []

        stu = quickest_route("smallSampleGraph.txt", "Manhattan", "LincolnCenter")
        print("Your shortest path: ", stu)
        assert stu == []

        stu = quickest_route("smallSampleGraph.txt", "LincolnCenter", "EmpireState")
        print("Your shortest path: ", stu)
        assert stu == [3, "LincolnCenter", "TimesSquare", "EmpireState"]

        stu = quickest_route("largeSampleGraph.txt", "LincolnCenter", "Brooklyn")
        print("Your shortest path: ", stu)
        assert stu == [10, "LincolnCenter", "TimesSquare", "EmpireState", "GramercyPark", "EastVillage",
                       "LowerEastSide", "Brooklyn"]
        stu = quickest_route("largeSampleGraph.txt", "Brooklyn", "Rochester")
        print("Your shortest path: ", stu)
        assert stu == []

if __name__ == "__main__":
    unittest.main()