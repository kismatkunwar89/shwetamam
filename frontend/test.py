import unittest
from Dashboard import Movie
import backend.database
import model.model



class test(unittest.TestCase):


    def setUp(self):
        self.s=Movie
        self.sorted_list=[1,2,3,4,5,6]

    def test_merge_sort_text(self):
        p_text = ['ashish', 'xeronimo', 'Bishesh', 'Prajwol', 'Adarsha', 'Bibek', 'Pandey']
        self.assertEqual(['Adarsha', 'Ashish','Bibek','Bishesh', 'Pandey', 'Prajwol','xeronimo'],
                         self.s.mergesort(p_text))



    def test_mergesort(self):
        num=[10,2,11,5,1]
        check=self.s.mergesort(num)
        self.assertEqual([1,2,5,10,11],check)

    def test_binarysearch(self):
        expected = '1'
        item=1
        actual = self.s.binary_room_number(self.sorted_list,item)
        self.assertNotEqual(expected, actual)

class Test_dbconect(unittest.TestCase):
    def setUp(self):
        self.a=backend.database.DBConnect()

    def test_insert(self):
        query="insert into new_table values(%s,%s,%s,%s,%s,%s,%s)"
        values=("nisma13","kapan","kkk","male",19,658,"3/1/21")
        self.a.insert(query,values)
        query1="select * from new_table where name='nisma13'"
        actual=self.a.view(query1)
        self.assertEqual([("nisma13","kapan","kkk","male",19,658,"3/1/21")],actual)

    def test_update(self):
        """
                Function to test if the update works or not.
        """
        query = "insert into new_table values(%s,%s,%s,%s,%s,%s,%s)"
        values = ("nisma467797", "kapan", "kkk", "male", 19,5032, "3/1/21")
        self.a.insert(query, values)
        query1 = "update new_table set address=%s where name=%s"
        values1 = ("maitidei","nisma467797")
        self.a.update(query1, values1)
        query2 = "select * from new_table where name='nisma467797'"
        actual = self.a.view(query2)
        self.assertEqual([("nisma467797", "maitidei", "kkk", "male", 19, 5032, "3/1/21")], actual)

class Test_User(unittest.TestCase):
    """
    Class Test_User tests the User class from model.user.
    """
    def setUp(self):
        self.obj_model = model.model.User()

    def test_set_id(self):
        self.obj_model.set_rno(1001)
        self.assertEqual(1001, self.obj_model.get_rno())

    def test_set_phone(self):
        with self.assertRaises(ValueError):
            self.obj_model.set_pno(100)



if __name__ == " __main__ ":
    unittest.main()
