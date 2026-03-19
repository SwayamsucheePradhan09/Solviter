import sys

html = []

html.append('''<div class="w-full max-w-7xl mx-auto px-2 md:px-10 py-2 flex justify-center"><div class="w-full flex flex-col mt-2 md:mt-5"><h2 class="text-[#181111] text-2xl font-bold leading-tight tracking-[-0.015em] px-2 pb-6 pt-2" style="font-family: &quot;Plus Jakarta Sans&quot;;">Student Picks</h2><div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 px-2">''')

star_svg = '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" class="w-3.5 h-3.5 text-yellow-400" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2 17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9 183.7-179.1c5-4.9 8.3-11.3 9.3-18.3 2.7-17.5-9.5-33.7-27-36.3z"></path></svg>'

outline_circle_svg = '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="text-[10px] text-gray-400" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12Z"></path></svg>'

map_pin_svg = '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 384 512" class="w-4 h-4 text-red-500 flex-shrink-0" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"></path></svg>'

clock_svg = '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="w-4 h-4 text-gray-400 flex-shrink-0" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M12.5 7.25a.75.75 0 0 0-1.5 0v5.5c0 .27.144.518.378.651l3.5 2a.75.75 0 0 0 .744-1.302L12.5 12.315V7.25Z"></path><path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Z"></path></svg>'

student_picks = [
    {"name": "Kake Di Hatti", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FKake%20Di%20Hatti.webp?alt=media&token=441fb516-d187-4931-87c2-2bfe0b31bdb2", "rating": "4.8", "reviews": "2.7k+", "cuisine": "North Indian", "addr": "3rd Floor, OEU Tower, KIIT Road, Patia", "time": "12:00 AM - 10:45 PM", "delay": "0"},
    {"name": "Mainland China", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FMainland%20China.webp?alt=media&token=ef2e7290-7c38-4136-8f79-4fb6f62f0b0a", "rating": "4.3", "reviews": "2.5k+", "cuisine": "Chinese", "addr": "The Crown Hotel, IRC Village, Nayapalli", "time": "12:00 PM - 11:00 PM", "delay": "80"},
    {"name": "Chai Break", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FChai%20Break.webp?alt=media&token=042e72e1-7e9c-4ab6-8e72-2a61fa6e5f3b", "rating": "4.3", "reviews": "2.2k+", "cuisine": "Multi-Cuisine", "addr": "KIIT Road, Chandaka Industrial Estate, Patia", "time": "11:00 AM - 10:45 PM", "delay": "160"},
    {"name": "The Big Bike Hub Cafe", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FThe%20Big%20Bike%20Hub%20Caf%C3%A9.webp?alt=media&token=bdbacf66-c02f-44a9-8377-f31d971fdb33", "rating": "4.3", "reviews": "1k+", "cuisine": "Cafe", "addr": "Patia, Above Suzuki Showroom", "time": "10:00 AM - 10:00 PM", "delay": "240"},
    {"name": "Kanika", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FKanika.webp?alt=media&token=5f6b0f62-b41f-407b-ae68-ac8802658fbd", "rating": "4.3", "reviews": "900+", "cuisine": "Odia", "addr": "Mayfair Lagoon, 8-B, Jaydev Vihar", "time": "12:00 PM - 11:00 PM", "delay": "320"},
    {"name": "Koraput Coffee", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FKoraput%20Coffee.webp?alt=media&token=d765f4ab-8934-4981-ae87-304c1a881557", "rating": "4.2", "reviews": "1k+", "cuisine": "Cafe", "addr": "Ekamra Kanan Botanical Gardens, Nayapalli", "time": "8:00 AM - 6:00 PM", "delay": "400"}
]

for p in student_picks:
    html.append(f'<div role="button" tabindex="0" class="flex flex-col rounded-xl shadow-sm border border-gray-100 bg-white overflow-hidden focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-200 font-[nunito] hover:shadow-md duration-200 transition-all ease-in-out cursor-pointer animate-fade-in-up hover:scale-[1.01]" style="animation-delay: {p["delay"]}ms;"><div class="relative w-full bg-gray-100 overflow-hidden"><img src="{p["img"]}" alt="{p["name"]}" class="w-full h-48 md:h-52 object-cover object-center transition-transform duration-300 ease-in-out group-hover:scale-[1.02]" loading="lazy"><div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md border border-gray-200 px-2.5 py-1 rounded-full flex items-center gap-1.5 shadow-sm font-[Poppins]">{star_svg}<span class="text-xs font-medium text-slate-800">{p["rating"]}</span>{outline_circle_svg}<span class="text-[11px] text-gray-600">{p["reviews"]} Reviews</span></div></div><div class="p-4 font-[poppins]"><div class="mt-2 w-full flex items-center justify-between gap-2"><h3 class="text-base font-semibold text-slate-900 leading-tight line-clamp-2 flex-1 min-w-0">{p["name"]}</h3><span class="inline-flex items-center text-[11px] font-medium text-purple-700 bg-purple-50 px-2.5 py-0.5 rounded-full border border-purple-100 whitespace-nowrap flex-shrink-0">{p["cuisine"]}</span></div><div class="mt-3 flex items-center justify-between text-xs text-gray-500"><div class="flex items-center gap-1 truncate">{map_pin_svg}<span class="truncate">{p["addr"]}</span></div><div class="flex items-center gap-1">{clock_svg}<span class="whitespace-nowrap">{p["time"]}</span></div></div></div></div>')

html.append('''</div><div class="flex flex-col items-center gap-4 mt-12 mb-10 font-[exo]"><button class="inline-flex items-center justify-center gap-2 px-4 py-2 sm:text-base font-medium text-white bg-gray-900 hover:bg-gray-800 rounded-full transition-all duration-300 shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"><span class="text-sm">Load More Restaurants</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="text-md" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path fill="none" d="M0 0h24v24H0z"></path><path d="M18 6.41 16.59 5 12 9.58 7.41 5 6 6.41l6 6z"></path><path d="m18 13-1.41-1.41L12 16.17l-4.59-4.58L6 13l6 6z"></path></svg></button></div></div></div><style jsx="true">
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        @keyframes fade-in-up {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fade-in {
          animation: fade-in 0.6s ease-out forwards;
        }
        .animate-fade-in-up {
          animation: fade-in-up 0.6s ease-out forwards;
          opacity: 0;
        }
        .animate-bounce {
          animation: bounce 1s infinite;
        }
        @keyframes bounce {
          0%,
          100% {
            transform: translateY(-25%);
            animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
          }
          50% {
            transform: translateY(0);
            animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
          }
        }
      </style><div class="w-full max-w-7xl mx-auto px-3 md:px-8 mt-8"><div class="w-full flex flex-col"><h2 class="text-[#181111] text-2xl md:text-3xl font-bold leading-tight tracking-[-0.015em] px-1 pb-6" style="font-family: &quot;Plus Jakarta Sans&quot;;">Popular Near Campus</h2><div class="grid grid-cols-2 lg:grid-cols-4 gap-5">''')

pop_near = [
    {"name": "The Aromas Multi Cuisine Restaurant", "img": "https://dineout-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/DINEOUT_ALL_RESTAURANTS/IMAGES/RESTAURANT_IMAGE_SERVICE/2024/8/22/efa40928-f579-4895-93ce-1dae63893263_20240822T063139928.jpg", "rating": "4.6", "cuisine": "Mughlai"},
    {"name": "Jagamara Food Court", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FJagamara%20Food%20Court%202.webp?alt=media&token=2ff42587-872b-4034-ae20-e595cf8b9e2a", "rating": "4.3", "cuisine": "Multi-Cuisine"},
    {"name": "Bocca Cafe", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FBocca%20Cafe.webp?alt=media&token=fff3ab45-168c-4907-a9c5-0ee4ce92a72d", "rating": "4.3", "cuisine": "Cafe"},
    {"name": "Biggies Burger", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FBiggies%20Burger.webp?alt=media&token=08205204-1a7f-4cdc-bef9-05bbd5f4c7ba", "rating": "4.3", "cuisine": "American"},
    {"name": "Anna's Biryani And Restaurant", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FAnna%E2%80%99s%20Biriyani%20%26%20Restaurant.png?alt=media&token=fade677c-175d-477e-881a-777685fd699d", "rating": "4.3", "cuisine": "Multi-Cuisine"},
    {"name": "Wow! Momo", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FWow!%20Momo.jpg?alt=media&token=256abfbe-9de7-4128-a138-1747ad1372de", "rating": "4.2", "cuisine": "Chinese"},
    {"name": "Adda Pan Asian", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FAdda%20Pan%20Asian.webp?alt=media&token=d8d17deb-5e91-49e9-ae68-ae86642f1b53", "rating": "4.2", "cuisine": "Multi-Cuisine"},
    {"name": "Scholars", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FScholars.jpg?alt=media&token=66bd407d-99c5-4c76-897a-93ea517e826e", "rating": "4.1", "cuisine": "Multi-Cuisine"},
    {"name": "Chai Sutta Bar", "img": "https://firebasestorage.googleapis.com/v0/b/menumate-ad653.firebasestorage.app/o/restaurants%2FChai%20Sutta%20Bar.webp?alt=media&token=acf13845-99b9-4d6b-8406-04326729895a", "rating": "4.1", "cuisine": "Cafe"}
]

for p in pop_near:
    html.append(f'<div class="flex flex-col rounded-xl overflow-hidden bg-white border border-gray-100 shadow-sm hover:shadow-md transition-all duration-200 cursor-pointer group hover:scale-[1.01] font-[poppins]"><div class="relative w-full aspect-square bg-gray-100 overflow-hidden"><img src="{p["img"]}" alt="{p["name"]}" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-300" loading="lazy"><div class="absolute top-2 left-2 bg-white/90 backdrop-blur-sm border border-gray-100 px-2 py-0.5 rounded-full flex items-center gap-1 shadow-sm">{star_svg}<span class="text-[11px] font-medium text-slate-700">{p["rating"]}</span></div></div><div class="p-3"><p class="text-sm font-semibold text-slate-900 truncate">{p["name"]}</p><p class="text-xs text-gray-500 mt-1 truncate">{p["cuisine"]}</p></div></div>')

html.append('''</div></div></div>''')

final_html = "".join(html)

with open('Bakery.html', 'r') as f:
    text = f.read()

start_idx = text.find('  <!-- Bakery Section Heading -->')
end_idx = text.find('  <!-- Footer -->')

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + final_html + "\n" + text[end_idx:]
    with open('Bakery.html', 'w') as f:
        f.write(new_text)
    print("Replaced successfully!")
else:
    print("Could not find boundaries")

