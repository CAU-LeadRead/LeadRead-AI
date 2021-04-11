import os


def others_name():
    base_dir = "./notes_copy"

    brands = os.listdir(base_dir)

    result = open("names.txt", "w", encoding="utf-8")
    for brand in brands:
        brand_n = brand.split(".")[0]
        brand_name = open("./names/" + brand_n + "_names.txt", "w", encoding="utf-8")
        brand_dir = os.path.join(base_dir, brand)
        with open(brand_dir, "r", encoding="utf-8") as f:
            names = f.readlines()[::4]
            # print(names)
            for name in names:
                brand_name.write(brand_n + " " + name)

        brand_name.close()


def joAndDip():
    brands = ["jomalone.txt", "Diptyque.txt"]
    for brand in brands:
        brand_n = brand.split(".")[0]
        brand_name = open("./names/" + brand_n + "_names.txt", "w", encoding="utf-8")
        # brand_dir = os.path.join(base_dir, brand)
        brand_dir = brand
        with open(brand_dir, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if "-" in line:
                    line = line[1:]
                    brand_name.write(brand_n + " " + line)

        brand_name.close()


def join_names():
    base_dir = "./names"

    brands = os.listdir(base_dir)

    result = open("names.txt", "w", encoding="utf-8")
    for brand in brands:
        brand_n = brand.split(".")[0]
        brand_dir = os.path.join(base_dir, brand)
        with open(brand_dir, "r", encoding="utf-8") as f:
            names = f.readlines()
            for name in names:
                result.write(name)

    result.close()


if __name__ == "__main__":
    join_names()