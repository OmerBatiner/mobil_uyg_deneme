from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from data_fetcher import get_stock_data
from data_analyzer import plot_stock_data, calculate_statistics
from notifier import send_notification

class StockApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Welcome to Stock App")
        layout.add_widget(self.label)
        
        self.currency_input = TextInput(hint_text="Currency")
        layout.add_widget(self.currency_input)
        
        self.amount_input = TextInput(hint_text="Amount", input_filter='int')
        layout.add_widget(self.amount_input)
        
        button = Button(text="Get Data")
        button.bind(on_press=self.update_label)
        layout.add_widget(button)
        
        invest_button = Button(text="Invest")
        invest_button.bind(on_press=self.invest)
        layout.add_widget(invest_button)
        
        self.image = Image()
        layout.add_widget(self.image)
        
        self.stats_label = Label(text="Statistics will be shown here")
        layout.add_widget(self.stats_label)
        
        return layout

    def update_label(self, instance):
        currency = self.currency_input.text
        data = get_stock_data(currency)
        plot_stock_data(data, currency)
        
        # Grafi i ekrana y kle
        self.image.source = f"{currency}_stock_plot.png"
        
        stats = calculate_statistics(data)
        self.label.text = f"{currency} Current Value: {data['Close'].iloc[-1]:.2f} TL"
        self.stats_label.text = (
            f"Mean Price: {stats['mean_price']:.2f}\n"
            f"Standard Deviation: {stats['std_dev']:.2f}\n"
            f"Price Change: {stats['price_change']:.2f}%"
        )
        
        #  rnek bildirim
        send_notification(f"{currency} Stock Alert", f"{currency} stock data updated")

    def invest__init__(self, instance):
        currency = self.currency_input.text
        amount = self.amount_input.text
        # Burada yat r m i lemini ger ekle tirebilirsiniz
        self.label.text = f"Invested {amount} in {currency}"

if __name__ == "__main__":
    StockApp().run()
