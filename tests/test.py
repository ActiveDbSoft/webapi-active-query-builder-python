from webapi_active_query_builder import *
import unittest

class QueryBuilderApiTests(unittest.TestCase):
    def setUp(self):

        self._api = ActiveQueryBuilderApi()
        self._transform = Transform()
        self._transform.guid = self._guid = "b3207f4f-b1f4-4dc2-979b-7724ed2d0221"
        self._transform.sql = self._sql = "select customer_id, first_name, last_name, create_date from customer"

    def tearDown(self):
        self._api = None
        self._transform = None

    def test_avg(self):
        avg = Totals()
        avg.field = "first_name"
        avg.aggregate = "avg"

        self._transform.totals = [avg]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select Avg(q.first_name) as first_nameavg From (Select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date From customer) q"
        self.assertEqual(result.totals.lower(), correct.lower())

    def test_count(self):
        count = Totals()
        count.field = "first_name"
        count.aggregate = "count"

        self._transform.totals = [count]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select Count(q.first_name) as first_namecount From (Select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date From customer) q"
        self.assertEqual(result.totals.lower(), correct.lower())

    def test_max(self):
        max = Totals()
        max.field = "first_name"
        max.aggregate = "max"

        self._transform.totals = [max]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select Max(q.first_name) as first_namemax From (Select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date From customer) q"
        self.assertEqual(result.totals.lower(), correct.lower())

    def test_min(self):
        min = Totals()
        min.field = "first_name"
        min.aggregate = "min"

        self._transform.totals = [min]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select Min(q.first_name) as first_namemin From (Select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date From customer) q"
        self.assertEqual(result.totals.lower(), correct.lower())

    def test_sum(self):
        sum = Totals()
        sum.field = "first_name"
        sum.aggregate = "sum"

        self._transform.totals = [sum]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select Sum(q.first_name) as first_namesum From (Select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date From customer) q"
        self.assertEqual(result.totals.lower(), correct.lower())

    def test_page(self):
        page = Pagination()
        page.skip = 2
        page.take = 3

        self._transform.pagination = page

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer limit 3 offset 2"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_order(self):
        order = Sorting()
        order.field = "customer_id"
        order.order = "asc"

        self._transform.sortings = [order]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select customer.customer_id, customer.first_name, customer.last_name, customer.create_date From customer order by customer.customer_id"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_order_desc(self):
        order = Sorting()
        order.field = "customer_id"
        order.order = "desc"

        self._transform.sortings = [order]

        result = self._api.transform_sql_post(self._transform)

        correct = "Select customer.customer_id, customer.first_name, customer.last_name, customer.create_date From customer order by customer.customer_id desc"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_hide_column(self):
        column = HiddenColumn()
        column.field = "first_name"

        self._transform.hidden_columns = [column]

        result = self._api.transform_sql_post(self._transform)

        correct = "select q.customer_id, q.last_name, q.create_date from (select customer.customer_id customer_id, customer.first_name first_name, customer.last_name last_name, customer.create_date create_date from customer) q"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_filter_contains(self):
        filter = ConditionGroup();

        condition = Condition()
        condition.field = "first_name"
        condition.condition_operator = "Contains"
        condition.values = ['Orlando']

        filter.conditions = [condition]

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer where customer.first_name like '%Orlando%'"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_filter_less(self):
        filter = ConditionGroup();

        condition = Condition()
        condition.field = "customer_id"
        condition.condition_operator = "Less"
        condition.values = [5]

        filter.conditions = [condition]

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer where customer.customer_id < 5"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_filter_between(self):
        filter = ConditionGroup();

        condition = Condition()
        condition.field = "customer_id"
        condition.condition_operator = "Between"
        condition.values = [1, 5]

        filter.conditions = [condition]

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer where customer.customer_id between 1 and 5"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_filter_is_not_null(self):
        filter = ConditionGroup();

        condition = Condition()
        condition.field = "customer_id"
        condition.condition_operator = "IsNotNull"

        filter.conditions = [condition]

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer where customer.customer_id is not null"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_condition_group(self):
        filter = ConditionGroup();

        conditionGroup = ConditionGroup();
        conditionGroup.junction_type = "And";

        condition1 = Condition()
        condition1.field = "customer_id"
        condition1.condition_operator = "IsNull"

        condition2 = Condition()
        condition2.field = "customer_id"
        condition2.condition_operator = "IsNotNull"

        conditionGroup.conditions = [condition1, condition2]

        filter.condition_groups = [conditionGroup]

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "select customer.customer_id, customer.first_name, customer.last_name, customer.create_date from customer where (customer.customer_id is null) and (customer.customer_id is not null)"
        self.assertEqual(result.sql.lower(), correct.lower())

    def test_invalid_column(self):
        filter = ConditionGroup();

        condition = Condition()
        condition.field = "id1"
        condition.condition = "IsNotNull"

        filter.conditions = [condition]        

        self._transform.filter = filter

        result = self._api.transform_sql_post(self._transform)

        correct = "QueryTransformer does't contain id1"
        self.assertEqual(result.error.lower(), correct.lower())

    def test_get_fields(self):
        query = SqlQuery()
        query.guid = self._guid
        query.text = self._sql

        fields = self._api.get_query_columns_post(query)    

        self.assertEqual(len(fields), 4)
        self.assertEqual("customer_id", fields[0].name.lower())
        self.assertEqual("smallint", fields[0].data_type)
        self.assertEqual("create_date", fields[3].name.lower())
        self.assertEqual("datetime", fields[3].data_type)

if __name__ == '__main__':
    unittest.main()
