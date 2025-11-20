import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import sys

DEFAULT_FILENAME = "supplies.csv" 

def main(csv_file):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        current_dir = os.getcwd()
        
    os.chdir(current_dir)
    print(f"📂 Робоча директорія: {current_dir}")

    if not os.path.exists(csv_file):
        print(f"❌ ПОМИЛКА: Файл '{csv_file}' не знайдено!")
        print(f"   Переконайтеся, що '{csv_file}' лежить у папці: {current_dir}")
        return

    try:
        df = pd.read_csv(csv_file)
        df.columns = df.columns.str.strip()
    except Exception as e:
        print(f"❌ Не вдалося прочитати CSV: {e}")
        return

    try:
        required = ['price_per_unit', 'quantity', 'supplier', 'category']
        missing = [col for col in required if col not in df.columns]
        if missing:
            print(f"❌ У файлі відсутні колонки: {missing}")
            print(f"   Наявні колонки: {list(df.columns)}")
            return

        mean_price = np.mean(df['price_per_unit'])
        median_qty = np.median(df['quantity'])
        df['total_price'] = df['quantity'] * df['price_per_unit']
        category_counts = df.groupby('category')['quantity'].sum()




        low_supply_path = os.path.join(current_dir, 'low_supply.csv')
        df[df['quantity'] < 100].to_csv(low_supply_path, index=False)
        print(f"✅ CSV збережено: {low_supply_path}")


        report_path = os.path.join(current_dir, 'report.txt')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"Mean Price: {mean_price:.2f}\nMedian Quantity: {median_qty:.2f}\n")
        print(f"✅ Звіт збережено: {report_path}")


        plt.figure(figsize=(8, 5))
        category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Total Quantity by Category')
        plt.tight_layout()
        plot_path = os.path.join(current_dir, 'category_distribution.png')
        plt.savefig(plot_path)
        print(f"✅ Графік збережено: {plot_path}")
        
    except Exception as e:
        print(f"❌ Сталася помилка під час обчислень: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("csv_file", help="Path to input CSV")
        args = parser.parse_args()
        target_file = args.csv_file
    else:
        print(f"⚠️ Запуск без аргументів. Використовую файл за замовчуванням: '{DEFAULT_FILENAME}'")
        target_file = DEFAULT_FILENAME
    
    main(target_file)