import generator as gen
import alerts_launcher as al
import alerts_sorter as aso

if __name__ == "__main__":
    #Get logs from generator automaton
    logs = gen.generate_logs(gen.state_machine, gen.NB_LOGS, gen.LOG_LENGTH)
    print("\n Logs : \n", logs)
    logs = gen.reformate_logs(logs)
    print("\n Reformated logs : \n", logs)

    #Get alerts from logs
    alerts = []
    for log in logs:
        if al.is_alert(log):
            alerts.append(log)

    print("\n Alerts : \n", alerts)

    attacks = []
    #Sort alerts to get attacks
    for alert in alerts:
        if aso.is_attack(alert):
            attacks.append(alert)

    print("\n Attacks : \n", attacks)
   