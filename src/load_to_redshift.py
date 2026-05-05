from src.load_phase.create_tables import vehicle_metrics, anomaly_summary, trip_metrics

def load_to_redshift():
    vehicle_metrics()
    anomaly_summary()
    trip_metrics()

if __name__=="__main__":
    load_to_redshift()