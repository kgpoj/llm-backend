data_fields = '''
"fullAddress",
"shortAddress",
"suburb",
"state",
"streetName",
"postcode",
"valuations": {{
    "sale": {{
        "confidence": The confidence meter shows how confident we are that the estimate is a good one. Our confidence level depends on how much data we have about the market and property.High confidence: We have a lot of market data, so the estimated value range is narrow.Medium confidence: We have some market data, so the estimated value range is average.Low confidence: We have less market data, so the estimated value range is wide.No estimate: We have no market data, so we can't estimate the property's value.
        "display": {{
            "lastUpdated",
            "value"
        }}
    }}:Estimated value for selling the property,
    "rental": {{
        "confidence",
        "display": {{
            "lastUpdated"
            "value"
        }}
    }}:Estimated value for renting the property,
}},
"attributes": {{
    "propertyType": The property type,e.g. "House",
    "bedrooms": Number of bedrooms,
    "bathrooms": Number of bathrooms,
    "carSpaces": Number of carSpaces,
    "landArea": Property area,
    "floorArea"
    "yearBuilt",
}},
"comparableMarketEvents": {{
    "buy": Similar properties currently for sale,
    "sold": Similar properties already sold,
    "rent": Similar properties available for rent,
    "leased": Similar properties already rented
}},
"recentSales": Recent sales information of the area where the property is located,
"propertyTimeline": {{
    "date": Sold date,
    "agency": Sold by,
    "price",
    "eventType",
}},
"marketInsights": {{
    "supplyDemand": {{
        "buy": {{
            "latest": Supply and demand for sales, including the latest supply change percentage and demand change percentage for sale,
        }}
        "rent": {{
            "latest": Supply and demand for rentals, including the latest supply change percentage and demand change percentage for rent,
        }}
    }},
    "medianData": {{
        "propertyType": The property type,e.g. "House",
        "bedrooms",
        "medianSoldPrice",
        "soldDataIngestDateDisplay",
        "soldProperties",
        "medianRentalPrice",
        "rentDataIngestDateDisplay",
        "rentalProperties",
    }}: median sold/rent price of property with same type and same number of bedrooms in the same suburb,
    "daysOnSiteYearly": {{
        "buy": Median days taken for sale transactions of similar properties in the same area,
        "rent": Median days taken for rental transactions of similar properties in the same area,
    }}
}}
'''
