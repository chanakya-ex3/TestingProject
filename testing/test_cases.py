from pandas import Period


test_cases = {
    "case1":{
        "total revenue by month":[(Period('2023-01', 'M'), 1200), (Period('2023-02', 'M'), 2050), (Period('2023-03', 'M'), 1050), (Period('2023-04', 'M'), 1200), (Period('2023-05', 'M'), 1200), (Period('2023-06', 'M'), 800), (Period('2023-07', 'M'), 950), (Period('2023-08', 'M'), 900)],
            "total revenue by product":[('Smartphone', 1600), ('Laptop', 1200), ('Refrigerator', 800), ('TV', 800), ('Tablet', 800), ('Gaming Console', 700), ('Air Purifier', 600), ('Camera', 500), ('Washing Machine', 500), ('Headphones', 450), ('Dishwasher', 400), ('Speaker', 400), ('Smartwatch', 250), ('Vacuum Cleaner', 200), ('Microwave', 150)],
            "total revenue by customer":[(201, 2950), (202, 2800), (204, 1300), (206, 800), (207, 500), (203, 450), (208, 400), (205, 150)],
            "top 10 customers by revenue":[(201, 2950), (202, 2800), (204, 1300), (206, 800), (207, 500), (203, 450), (208, 400), (205, 150)]
    },
    "case2":{
        "total revenue by month":[(Period('2023-01', 'M'), 750), (Period('2023-02', 'M'), 1300), (Period('2023-03', 'M'), 600), (Period('2023-04', 'M'), 250), (Period('2023-05', 'M'), 110), (Period('2023-06', 'M'), 220), (Period('2023-07', 'M'), 2800), (Period('2023-08', 'M'), 450)],
        "total revenue by product":[('Smartphone', 1600), ('Laptop', 1200), ('Refrigerator', 800), ('Air Purifier', 600), ('Washing Machine', 500), ('Headphones', 450), ('Dishwasher', 400), ('Coffee Maker', 200), ('Electric Shaver', 160), ('Microwave', 150), ('Blender', 150), ('Toaster', 100), ('Iron', 80), ('Hair Dryer', 60), ('Kettle', 30)],
        "total revenue by customer":[(314, 1600), (313, 1200), (303, 800), (301, 600), (304, 500), (315, 450), (305, 400), (306, 200), (312, 160), (307, 150), (302, 150), (308, 100), (310, 80), (311, 60), (309, 30)],
        "top 10 customers by revenue":[(314, 1600), (313, 1200), (303, 800), (301, 600), (304, 500), (315, 450), (305, 400), (306, 200), (312, 160), (307, 150)]},
    "case3":{
        "total revenue by month":[(Period('2023-08', 'M'), 250), (Period('2023-09', 'M'), 1300), (Period('2023-10', 'M'), 1500), (Period('2023-11', 'M'), 600), (Period('2023-12', 'M'), 750), (Period('2024-01', 'M'), 1300), (Period('2024-02', 'M'), 600), (Period('2024-03', 'M'), 250)],
        "total revenue by product":[('Tablet', 800), ('TV', 800), ('Refrigerator', 800), ('Gaming Console', 700), ('Air Purifier', 600), ('Washing Machine', 500), ('Camera', 500), ('Speaker', 400), ('Dishwasher', 400), ('Smartwatch', 250), ('Coffee Maker', 200), ('Vacuum Cleaner', 200), ('Blender', 150), ('Microwave', 150), ('Toaster', 100)],
        "total revenue by customer":[(402, 800), (405, 800), (410, 800), (404, 700), (408, 600), (403, 500), (411, 500), (406, 400), (412, 400), (401, 250), (407, 200), (413, 200), (409, 150), (414, 150), (415, 100)],
        "top 10 customers by revenue":[(402, 800), (405, 800), (410, 800), (404, 700), (408, 600), (403, 500), (411, 500), (406, 400), (412, 400), (401, 250)]
        },
    "case4":{
        "total revenue by month":[(Period('2023-01', 'M'), 110), (Period('2023-02', 'M'), 220), (Period('2023-03', 'M'), 2800), (Period('2023-04', 'M'), 700), (Period('2023-05', 'M'), 1300), (Period('2023-06', 'M'), 1500), (Period('2023-07', 'M'), 600), (Period('2023-08', 'M'), 600)],
        "total revenue by product":[('Smartphone', 1600), ('Laptop', 1200), ('Tablet', 800), ('TV', 800), ('Gaming Console', 700), ('Air Purifier', 600), ('Camera', 500), ('Headphones', 450), ('Speaker', 400), ('Smartwatch', 250), ('Vacuum Cleaner', 200), ('Electric Shaver', 160), ('Iron', 80), ('Hair Dryer', 60), ('Kettle', 30)],
        "total revenue by customer":[(506, 1600), (505, 1200), (509, 800), (512, 800), (511, 700), (515, 600), (510, 500), (507, 450), (513, 400), (508, 250), (514, 200), (504, 160), (502, 80), (503, 60), (501, 30)],
        "top 10 customers by revenue":[(506, 1600), (505, 1200), (509, 800), (512, 800), (511, 700), (515, 600), (510, 500), (507, 450), (513, 400), (508, 250)]
        },
    "case5":{
        "total revenue by month":[(Period('2023-08', 'M'), 150), (Period('2023-09', 'M'), 1300), (Period('2023-10', 'M'), 600), (Period('2023-11', 'M'), 250), (Period('2023-12', 'M'), 110), (Period('2024-01', 'M'), 220), (Period('2024-02', 'M'), 2800), (Period('2024-03', 'M'), 700)],
        "total revenue by product":[('Smartphone', 1600), ('Laptop', 1200), ('Refrigerator', 800), ('Washing Machine', 500), ('Headphones', 450), ('Dishwasher', 400), ('Smartwatch', 250), ('Coffee Maker', 200), ('Electric Shaver', 160), ('Blender', 150), ('Microwave', 150), ('Toaster', 100), ('Iron', 80), ('Hair Dryer', 60), ('Kettle', 30)],
        "total revenue by customer":[(613, 1600), (612, 1200), (602, 800), (603, 500), (614, 450), (604, 400), (615, 250), (605, 200), (611, 160), (601, 150), (606, 150), (607, 100), (609, 80), (610, 60), (608, 30)],
        "top 10 customers by revenue":[(613, 1600), (612, 1200), (602, 800), (603, 500), (614, 450), (604, 400), (615, 250), (605, 200), (611, 160), (601, 150)]
    }
}