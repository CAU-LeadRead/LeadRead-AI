import os
import csv


def others_name():
    base_dir = "./notes_copy"

    brands = os.listdir(base_dir)

    result = open("database.csv", "w", encoding="utf-8")
    writer = csv.writer(result)
    for brand in brands:
        brand_n = brand.split(".")[0]
        brand_dir = os.path.join(base_dir, brand)
        with open(brand_dir, "r", encoding="utf-8") as f:
            lines = f.readlines()
            names = lines[::4]
            tops = lines[1::4]
            mid = lines[2::4]
            base = lines[3::4]
            for i in range(len(tops)):
                writer.writerow([brand_n, names[i], "top", tops[i]])

            # print(names)
            for name in names:
                writer.writerow(brand_n + " " + name)

    result.close()


others_name()
