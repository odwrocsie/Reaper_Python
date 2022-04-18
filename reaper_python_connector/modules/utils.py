

class Markers:
    markers_dict = {}

    def add_marker(self, project):
        first_marker_start_in_sec = 40000
        marker = project.add_marker(first_marker_start_in_sec + i * 50)
        first_marker_idx = marker.index

    def set_markers(self):
        for markerIdx in range(first_marker_idx, first_marker_idx + len(set_angles)):
            tmp = markerIdx - first_marker_idx
            marker = project.markers[markerIdx - 1]
            marker_position = marker.position
            change_param(marker_position, set_angles[tmp], referenceTrack)